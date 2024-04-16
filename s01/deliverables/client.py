import socket
import sys


def main(web_address, port):
    # Create a socket object
    s = socket.socket()
    s.connect((web_address, port))

    # create, format, and send the request
    request = 'GET / HTTP/1.1\r\nHost: %s\r\nConnection: close\r\n\r\n' % web_address
    request = request.encode('ISO 8859-1')
    s.sendall(request)

    # receive and print the response
    response = b''
    while True:
        data = s.recv(300)
        print(response)
        if len(data) == 0:
            break
        response += data

    response = response.decode('ISO 8859-1')
    s.close()
    print(response)



if __name__ == "__main__":
    web_address = sys.argv[1]
    port = sys.argv[2]
    main(web_address, int(port))
