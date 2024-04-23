
checksums=[]
for i in range(10):
    with open(f"tcp_data/tcp_addrs_{i}.txt", "r") as fa:
        ip1, ip2 = fa.read().split()

    with open(f"tcp_data/tcp_data_{i}.dat", "rb") as fp:
        tcp_data = fp.read()
        tcp_checksum = tcp_data[16:18]
        tcp_length = len(tcp_data)

    checksums.append((i, tcp_checksum, ip1, ip2, tcp_length, tcp_data))

print("\n".join("".join(f"{i}\t" for i in checksum) for checksum in checksums))
