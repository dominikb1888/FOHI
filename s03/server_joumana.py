import socket
import os
import sys

def get_mime_type(filename):
    """Determine the type of data in the file, HTML or text"""
    _, ext = os.path.splitext(filename)
    return "text/html" if ext == ".html" else "text/plain"

def read_file(filename):
    """Read the data from the named file"""
    try:
        with open(filename, "rb") as file:
            return file.read()
    except FileNotFoundError:
        return None

def handle_request(request):
    """
    Parse the request to get the file name
    Strip the path off
    Build an HTTP response packet with the file data in the payload
    """
    parts = request.split()
    if len(parts) < 2 or parts[0] != "GET":
        return None
    filename = parts[1].lstrip("/")

    
    file_content = read_file(filename)
    if file_content is None:
        return ("HTTP/1.1 404 Not Found\r\n"
                "Content-Type: text/plain\r\n"
                "Content-Length: 13\r\n"
                "Connection: close\r\n\r\n"
                "404 Not Found").encode()

    mime_type = get_mime_type(filename)
    response_header = (f"HTTP/1.1 200 OK\r\n"
                       f"Content-Type: {mime_type}\r\n"
                       f"Content-Length: {len(file_content)}\r\n"
                       "Connection: close\r\n\r\n")

    return response_header.encode() + file_content

def start_server(port=28333):
    with socket.socket() as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('', port))
        s.listen()
        print(f"Server started on port {port}")

        while True:
            conn, addr = s.accept()
            print(f"Connected by {addr}")

            request = ""
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                request += data.decode("ISO-8859-1")
                if "\r\n\r\n" in request:
                    break

            response = handle_request(request)
            if response:
                conn.sendall(response)
            conn.close()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print("Invalid port number. Using default port 28333.")
            port = 28333
    else:
        port = 28333  # Default port

    start_server(port)
