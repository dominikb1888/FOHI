import socket
import os

# Function to handle incoming requests
def handle_request(client_socket):
    # Receive request data
    request_data = b""
    while True:
        data = client_socket.recv(4096)
        if not data:
            break
        request_data += data
        if b"\r\n\r\n" in request_data:
            break

    # Parse the HTTP request
    request_lines = request_data.decode("ISO-8859-1").split("\r\n")
    request_method, path, _ = request_lines[0].split(" ")

    # Strip path to filename
    filename = os.path.basename(path)

    # Set server root directory
    server_root = os.path.abspath('.')

    # Construct full file path
    file_path = os.path.join(server_root, filename)

    # Check if file exists
    if os.path.isfile(file_path):
        # Determine MIME type
        _, file_extension = os.path.splitext(filename)
        mime_types = {
            ".txt": "text/plain",
            ".html": "text/html"
            # Add more MIME types as needed
        }
        content_type = mime_types.get(file_extension, "application/octet-stream")

        # Read file data
        with open(file_path, "rb") as file:
            data = file.read()

        # Craft HTTP response
        response = f"HTTP/1.1 200 OK\r\n"
        response += f"Content-Type: {content_type}\r\n"
        response += f"Content-Length: {len(data)}\r\n"
        response += "Connection: close\r\n\r\n"
        response = response.encode("ISO-8859-1") + data

    else:
        # File not found, send 404 response
        response = "HTTP/1.1 404 Not Found\r\n"
        response += "Content-Type: text/plain\r\n"
        response += "Content-Length: 13\r\n"
        response += "Connection: close\r\n\r\n"
        response += "404 Not found"
        response = response.encode("ISO-8859-1")

    # Send response
    client_socket.sendall(response)

# Main function
def main():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Set socket options to reuse address
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Specify host and port
    host = "localhost"
    port = 33490

    # Bind the socket to the address
    server_socket.bind((host, port))

    # Listen for incoming connections
    server_socket.listen()

    print(f"Server listening on {host}:{port}...")

    try:
        while True:
            # Accept incoming connection
            client_socket, client_address = server_socket.accept()
            print(f"Connection from {client_address}")

            # Handle the request
            handle_request(client_socket)

            # Close the client socket
            client_socket.close()

    except KeyboardInterrupt:
        print("Server shutting down...")
        server_socket.close()

if __name__ == "__main__":
    main()
