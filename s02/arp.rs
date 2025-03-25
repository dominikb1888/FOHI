use pnet::datalink::{self, Channel::Ethernet, Config, NetworkInterface};
use pnet::packet::{Packet, arp::{ArpHardwareTypes, ArpOperations, ArpPacket, MutableArpPacket}, ethernet::{EtherTypes, EthernetPacket, MutableEthernetPacket}};
use pnet::util::MacAddr;
use std::net::Ipv4Addr;
use std::time::Duration;
use std::thread;
use std::collections::HashSet;

fn send_arp_request(interface: &NetworkInterface, target_ip: Ipv4Addr) {
    let source_mac = interface.mac.unwrap();
    let source_ip = match interface.ips.iter().find(|ip| ip.is_ipv4()) {
        Some(ip) => match ip.ip() {
            std::net::IpAddr::V4(v4) => v4,
            _ => return,
        },
        None => return,
    };

    let (mut tx, mut rx) = match datalink::channel(interface, Config::default()) {
        Ok(Ethernet(tx, rx)) => (tx, rx),
        _ => panic!("Failed to create channel"),
    };

    let mut ethernet_buffer = [0u8; 42]; // Ethernet + ARP packet size
    let mut arp_buffer = [0u8; 28];

    let mut ethernet_packet = MutableEthernetPacket::new(&mut ethernet_buffer).unwrap();
    ethernet_packet.set_destination(MacAddr::broadcast());
    ethernet_packet.set_source(source_mac);
    ethernet_packet.set_ethertype(EtherTypes::Arp);

    let mut arp_packet = MutableArpPacket::new(&mut arp_buffer).unwrap();
    arp_packet.set_hardware_type(ArpHardwareTypes::Ethernet);
    arp_packet.set_protocol_type(EtherTypes::Ipv4);
    arp_packet.set_hw_addr_len(6);
    arp_packet.set_proto_addr_len(4);
    arp_packet.set_operation(ArpOperations::Request);
    arp_packet.set_sender_hw_addr(source_mac);
    arp_packet.set_sender_proto_addr(source_ip);
    arp_packet.set_target_hw_addr(MacAddr::zero());
    arp_packet.set_target_proto_addr(target_ip);

    ethernet_packet.set_payload(arp_packet.packet());

    tx.send_to(ethernet_packet.packet(), None).unwrap();

    let mut discovered_hosts = HashSet::new();
    let timeout = std::time::Instant::now() + Duration::from_secs(5);

    while std::time::Instant::now() < timeout {
        if let Ok(packet) = rx.next() {
            if let Some(ethernet) = EthernetPacket::new(packet) {
                if ethernet.get_ethertype() == EtherTypes::Arp {
                    if let Some(arp) = ArpPacket::new(ethernet.payload()) {
                        if arp.get_operation() == ArpOperations::Reply {
                            discovered_hosts.insert((arp.get_sender_proto_addr(), arp.get_sender_hw_addr()));
                        }
                    }
                }
            }
        }
    }

    for (ip, mac) in discovered_hosts {
        println!("Discovered: {} - {}", ip, mac);
    }
}

fn get_interface(name: &str) -> Option<NetworkInterface> {
    datalink::interfaces()
        .into_iter()
        .find(|iface| iface.name == name)
}

fn main() {
    let iface_name = "en0"; // Change to your interface
    if let Some(interface) = get_interface(iface_name) {
        println!("Scanning network...");

        for i in 1..=254 {
            let target_ip = Ipv4Addr::new(172, 23, 4, i); // Adjust subnet as needed
            send_arp_request(&interface, target_ip);
            thread::sleep(Duration::from_millis(50));
        }
    } else {
        eprintln!("Interface not found!");
    }
}

