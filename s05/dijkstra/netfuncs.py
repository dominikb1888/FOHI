import sys
import json

def ipv4_to_value(ipv4_addr: str) -> int:
    """
    Convert a dots-and-numbers IP address to a single 32-bit numeric
    value of integer type. Returns an integer type.

    Example:

    ipv4_addr: "255.255.0.0"
    return:    4294901760  (Which is 0xffff0000 hex)

    ipv4_addr: "1.2.3.4"
    return:    16909060  (Which is 0x01020304 hex)
    """
    a,b,c,d = [int(s) for s in ipv4_addr.split(".")]
    return (a << 24) | (b << 16) | (c << 8) | d


def value_to_ipv4(addr) -> str:
    """
    Convert a single 32-bit numeric value of integer type to a
    dots-and-numbers IP address. Returns a string type.

    Example:

    There is only one input value, but it is shown here in 3 bases.

    addr:   0xffff0000 0b11111111111111110000000000000000 4294901760
    return: "255.255.0.0"

    addr:   0x01020304 0b00000001000000100000001100000100 16909060
    return: "1.2.3.4"
    """
    return ".".join(str((addr >> i) & 0xff) for i in [24,16,8,0])

def get_subnet_mask_value(slash: str) -> int:
    """
    Given a subnet mask in slash notation, return the value of the mask
    as a single number of integer type. The input can contain an IP
    address optionally, but that part should be discarded.

    Returns an integer type.

    Example:

    There is only one return value, but it is shown here in 3 bases.

    slash:  "/16"
    return: 0xffff0000 0b11111111111111110000000000000000 4294901760

    slash:  "10.20.30.40/23"
    return: 0xfffffe00 0b11111111111111111111111000000000 4294966784
    """
    # _, nbits = slash.split('/')
    # return int("1" * int(nbits) + "0" * (32- int(nbits)), 2)
    netmask = int(slash.split("/")[1])
    return (1 << 32) - (1 << (32 - netmask))

def ips_same_subnet(ip1: str, ip2: str, slash: str) -> bool:
    """
    Given two dots-and-numbers IP addresses and a subnet mask in slash
    notataion, return true if the two IP addresses are on the same
    subnet.

    Returns a boolean.

    FOR FULL CREDIT: this must use your get_subnet_mask_value() and
    ipv4_to_value() functions. Don't do it with pure string
    manipulation.

    This needs to work with any subnet from /1 to /31

    Example:

    ip1:    "10.23.121.17"
    ip2:    "10.23.121.225"
    slash:  "/23"
    return: True

    ip1:    "10.23.230.22"
    ip2:    "10.24.121.225"
    slash:  "/16"
    return: False
    """
    netmask = get_subnet_mask_value(slash)
    return get_network(ipv4_to_value(ip1), netmask) == get_network(ipv4_to_value(ip2), netmask)

def get_network(ip_value: int, netmask: int) -> int:
    """
    Return the network portion of an address value as integer type.

    Example:

    ip_value: 0x01020304
    netmask:  0xffffff00
    return:   0x01020300
    """
    return netmask & ip_value

def find_router_for_ip(routers: dict, ip: str):
    """
    Search a dictionary of routers (keyed by router IP) to find which
    router belongs to the same subnet as the given IP.

    Return None if no routers is on the same subnet as the given IP.

    FOR FULL CREDIT: you must do this by calling your ips_same_subnet()
    function.

    Example:

    [Note there will be more data in the routers dictionary than is
    shown here--it can be ignored for this function.]

    routers: {
        "1.2.3.1": {
            "netmask": "/24"
        },
        "1.2.4.1": {
            "netmask": "/24"
        }
    }
    ip: "1.2.3.5"
    return: "1.2.3.1"


    routers: {
        "1.2.3.1": {
            "netmask": "/24"
        },
        "1.2.4.1": {
            "netmask": "/24"
        }
    }
    ip: "1.2.5.6"
    return: None
    """
    for router, config in routers.items():
        if ips_same_subnet(router, ip, config['netmask']):
            return router

    return None



# Uncomment this code to have it run instead of the real main.
# Be sure to comment it back out before you submit!
def my_tests():
    print("-------------------------------------")
    print("This is the result of my custom tests")
    print("-------------------------------------")

    print("ipv4_to_value")
    assert ipv4_to_value("255.255.0.0") == 4294901760
    assert ipv4_to_value("1.2.3.4") == 16909060

    print("value_to_ipv4")
    assert value_to_ipv4(0xffff0000) == "255.255.0.0"
    assert value_to_ipv4(0b11111111111111110000000000000000) == "255.255.0.0"
    assert value_to_ipv4(4294901760) == "255.255.0.0"

    assert value_to_ipv4(0x01020304) == "1.2.3.4"
    assert value_to_ipv4(0b00000001000000100000001100000100) == "1.2.3.4"
    assert value_to_ipv4(16909060) == "1.2.3.4"

    print("get_subnet_mask_value")
    assert  get_subnet_mask_value("/16") == 0xffff0000
    assert  get_subnet_mask_value("/16") == 0b11111111111111110000000000000000
    assert  get_subnet_mask_value("/16") == 4294901760

    assert  get_subnet_mask_value("10.20.30.40/23") == 0xfffffe00
    assert  get_subnet_mask_value("10.20.30.40/23") == 0b11111111111111111111111000000000
    assert  get_subnet_mask_value("10.20.30.40/23") == 4294966784

    print("ips_same_subnet")
    assert ips_same_subnet("10.23.121.17", "10.23.121.225", "/23") == True
    assert ips_same_subnet("10.23.230.22", "10.24.121.225", "/16") == False

    print("get_network")
    assert get_network(0x01020304, 0xffffff00) == 0x01020300

    routers = {
        "1.2.3.1": {
            "netmask": "/24"
        },
        "1.2.4.1": {
            "netmask": "/24"
        }
    }
    ip = "1.2.3.5"
    assert find_router_for_ip(routers, ip) == "1.2.3.1"

    routers = {
        "1.2.3.1": {
            "netmask": "/24"
        },
        "1.2.4.1": {
            "netmask": "/24"
        }
    }
    ip = "1.2.5.6"
    assert find_router_for_ip(routers, ip) == None


## -------------------------------------------
## Do not modify below this line
##
## But do read it so you know what it's doing!
## -------------------------------------------

def usage():
    print("usage: netfuncs.py infile.json", file=sys.stderr)

def read_routers(file_name):
    with open(file_name) as fp:
        json_data = fp.read()

    return json.loads(json_data)

def print_routers(routers):
    print("Routers:")

    routers_list = sorted(routers.keys())

    for router_ip in routers_list:

        # Get the netmask
        slash_mask = routers[router_ip]["netmask"]
        netmask_value = get_subnet_mask_value(slash_mask)
        netmask = value_to_ipv4(netmask_value)

        # Get the network number
        router_ip_value = ipv4_to_value(router_ip)
        network_value = get_network(router_ip_value, netmask_value)
        network_ip = value_to_ipv4(network_value)

        print(f" {router_ip:>15s}: netmask {netmask}: " \
            f"network {network_ip}")

def print_same_subnets(src_dest_pairs):
    print("IP Pairs:")

    src_dest_pairs_list = sorted(src_dest_pairs)

    for src_ip, dest_ip in src_dest_pairs_list:
        print(f" {src_ip:>15s} {dest_ip:>15s}: ", end="")

        if ips_same_subnet(src_ip, dest_ip, "/24"):
            print("same subnet")
        else:
            print("different subnets")

def print_ip_routers(routers, src_dest_pairs):
    print("Routers and corresponding IPs:")

    all_ips = sorted(set([i for pair in src_dest_pairs for i in pair]))

    router_host_map = {}

    for ip in all_ips:
        router = str(find_router_for_ip(routers, ip))

        if router not in router_host_map:
            router_host_map[router] = []

        router_host_map[router].append(ip)

    for router_ip in sorted(router_host_map.keys()):
        print(f" {router_ip:>15s}: {router_host_map[router_ip]}")

def main(argv):
    if "my_tests" in globals() and callable(my_tests):
        my_tests()
        return 0

    try:
        router_file_name = argv[1]
    except:
        usage()
        return 1

    json_data = read_routers(router_file_name)

    routers = json_data["routers"]
    src_dest_pairs = json_data["src-dest"]

    print_routers(routers)
    print()
    print_same_subnets(src_dest_pairs)
    print()
    print_ip_routers(routers, src_dest_pairs)

if __name__ == "__main__":
    sys.exit(main(sys.argv))

