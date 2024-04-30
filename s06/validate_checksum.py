import os
import struct
import socket

def read_ipv4_addresses(file_path):
    with open(f"tcp_data/{file_path}", 'r') as file:
        lines = file.readlines()
        src_ip, dst_ip = lines[0].split()[0], lines[0].split()[1]
    return src_ip, dst_ip

def calculate_checksum(packet):
    if len(packet) % 2 != 0:
        packet += b'\x00'  # Padding if length is odd
    checksum = 0
    for i in range(0, len(packet), 2):
        word = (packet[i] << 8) + packet[i+1]
        checksum += word
        if checksum > 0xFFFF:
            checksum = (checksum & 0xFFFF) + 1
    return ~checksum & 0xFFFF

def validate_tcp_packet(ip_file, tcp_file):
    src_ip, dst_ip = read_ipv4_addresses(ip_file)

    with open(f"tcp_data/{tcp_file}", 'rb') as file:
        tcp_packet = file.read()

    tcp_header = tcp_packet[:20]  # Assuming TCP header length is 20 bytes
    payload = tcp_packet[20:]

    # Calculate TCP checksum
    pseudo_header = struct.pack('!4s4sBBH',
                                socket.inet_aton(src_ip),
                                socket.inet_aton(dst_ip),
                                0, 6, len(tcp_packet))
    pseudo_packet = pseudo_header + tcp_packet
    checksum = calculate_checksum(pseudo_packet)

    # Extract checksum from TCP header
    received_checksum = struct.unpack('!H', tcp_header[16:18])[0]

    # Compare checksums
    if checksum == received_checksum:
        return "PASS"
    else:
        return "FAIL"

# Find all files starting with "tcp_data_" in the current directory
tcp_files = list(os.listdir("tcp_data"))

# Iterate through each pair of files
for tcp_file in tcp_files:
    # Extract file number from tcp_file name
    file_number = tcp_file.split("_")[-1].split(".")[0]
    ip_file = f"tcp_addrs_{file_number}.txt"

    # Validate TCP packet and print result
    result = validate_tcp_packet(ip_file, tcp_file)
    print(f"Validation for {tcp_file}: {result}")
