import os
import struct

def calculate_checksum(data):
    """
    Calculate the 16-bit one's complement checksum of the given data.
    :param data: bytes, the input data to calculate the checksum for.
    :return: int, the calculated checksum.
    """
    if len(data) % 2 != 0:
        # Pad with a zero byte if the length is odd
        data += b'\x00'

    # Initialize the sum
    checksum = 0

    # Process each 16-bit word
    for i in range(0, len(data), 2):
        word = (data[i] << 8) + data[i + 1]
        checksum += word

    # Fold the carry bits
    while checksum >> 16:
        checksum = (checksum & 0xFFFF) + (checksum >> 16)

    # Take the one's complement
    checksum = ~checksum & 0xFFFF

    return checksum


def tcp_checksum(source_ip, dest_ip, tcp_data):
    """
    Calculate the TCP checksum for the given TCP segment.
    :param source_ip: str, source IP address (e.g., "192.168.1.1").
    :param dest_ip: str, destination IP address (e.g., "192.168.1.2").
    :param tcp_data: bytes, the TCP header and payload.
    :return: int, the calculated TCP checksum.
    """
    # Convert IP addresses to binary format
    source_ip_bin = bytes(map(int, source_ip.split('.')))
    dest_ip_bin = bytes(map(int, dest_ip.split('.')))

    # Construct the pseudo-header
    pseudo_header = (
        source_ip_bin +          # Source IP address
        dest_ip_bin +            # Destination IP address
        b'\x00\x06' +            # Protocol (TCP = 6)
        struct.pack('!H', len(tcp_data))  # TCP length
    )

    # Combine pseudo-header and TCP data
    combined_data = pseudo_header + tcp_data

    # Calculate the checksum
    return calculate_checksum(combined_data)

def ip_addr_to_binary(ipaddr):
    ipseg = list(map(int, ipaddr.split(".")))
    return (ipseg[0] << 24) | (ipseg[1] << 16) | (ipseg[2] << 8) | ipseg[3]


def process_tcp_data(folder_path):
    """
    Process all TCP data files in the specified folder to validate checksums.
    Print "Valid" or "Invalid" for each file.
    :param folder_path: str, path to the folder containing the TCP data files.
    """
    for i in range(10):  # Assuming there are 10 .dat files
        # File path
        data_file = os.path.join(folder_path, f"tcp_data_{i}.dat")
        addrs_file = os.path.join(folder_path, f"tcp_addrs_{i}.txt")
        # Read the raw TCP packet from the .dat file
        with open(data_file, 'rb') as f:
            packet = f.read()

        with open(addrs_file, 'r') as f:
            addrs = f.read()

        src, dest = addrs.split()
        # Extract the IP header fields
        # 1. Convert ip address to bytes for both src and dest address
        # 2. Add Zero -> 0x00
        # 3. PTCL -> 0x06
        # 4. TCP Packet Length
        # Extract the embedded checksum from the TCP header
        tcp_checksum_embedded = struct.unpack('!H', packet[16:18])[0]

        # Temporarily set the checksum field to zero for calculation
        tcp_segment_zeroed = packet[:16] + b'\x00\x00' + packet[18:]


        # Calculate the correct checksum
        calculated_checksum = tcp_checksum(src, dest, tcp_segment_zeroed)

        # Compare the checksums
        is_valid = calculated_checksum == tcp_checksum_embedded

        # Print the result
        print(f"{'PASS' if is_valid else 'FAIL'} | C: {calculated_checksum} | E: {tcp_checksum_embedded}")


# Example usage
if __name__ == "__main__":
    # Path to the folder containing the TCP data files
    folder_path = "./tcp_data"

    # Process all TCP data files
    process_tcp_data(folder_path)
