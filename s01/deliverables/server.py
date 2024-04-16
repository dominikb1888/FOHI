import sys
import socket

def main(port):
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('', port))
    s.listen()
    new_conn = s.accept()
    new_socket = new_conn[0]

    while True:
        data = new_socket.recv(4096)
        data += data
        response = 'HTTP/1.1 200 OK\r\n\r\nHello, World!'
        new_socket.sendall(response.encode('ISO 8859-1'))
        new_socket.close()


if __name__ == "__main__":
    port = sys.argv[1]
    main(int(port))
