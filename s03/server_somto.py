import socket
import os
import sys
from datetime import datetime


def get_mime_type(file_name):
    extension = os.path.splitext(file_name)[1]
    return {
        ".html": "text/html",
        ".txt": "text/plain",
    }.get(extension, "application/octet-stream")


def safe_join(base, *paths):
    path = os.path.join(base, *paths)
    return os.path.abspath(path) if path.startswith(os.path.abspath(base)) else None


def serve_file(file_path, server_root):
    # Check: if file path is valid and within the server root directory
    if file_path == "/" or file_path == "":
        file_path = "/index.html"
    abs_path = safe_join(server_root, file_path.lstrip("/"))

    status_line = ""
    response_headers = ""
    body = ""

    # Check: if the path does not exist
    if not abs_path or not os.path.exists(abs_path):
        status_line = "HTTP/1.1 404 Not Found"
        response_headers = "Content-Type: text/html"
        body = "<html><body><h1>404 Not Found</h1><p>Page not found.</p></body></html>"
        body = body.encode("utf-8")

    # Check: if the path is a directory
    elif os.path.isdir(abs_path):
        status_line = "HTTP/1.1 403 Forbidden"
        response_headers = "Content-Type: text/html"
        body = "<html><body><h1>Action Not Permitted</h1><p>You are trying to access a directory.</p></body></html>"
        body = body.encode("utf-8")

    # Serve the file
    else:
        with open(abs_path, "rb") as file:
            body = file.read()
        mime_type = get_mime_type(file_path)
        status_line = "HTTP/1.1 200 OK"
        response_headers = (
            f"""
                Content-Type: {mime_type}
                Content-Length: {len(body)}
            """)

    full_response = (
        f"{status_line}\r\n{response_headers}\r\n\r\n".encode("utf-8") + body
    )
    return full_response, status_line, response_headers


def start_server(server_root, port=28333):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(("", port))
        s.listen()
        print(f"Server started on port {port}. Live on http://localhost:{port}\n")

        while True:
            conn, addr = s.accept()
            request = conn.recv(1024).decode("utf-8")
            file_path = request.split(" ")[1]
            response, status_line, response_headers = serve_file(file_path, server_root)
            response_status = (
                f"{status_line.split(' ')[1]} {' '.join(status_line.split(' ')[2:])}"
            )
            metadata = response_headers.replace("Content-", "Content-")

            # Current timestamp
            current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Logging to terminal
            print(f"{current_timestamp}\nConnection received from {addr}")
            print(f"Request: {request.splitlines()[0]}")
            print(f"Response: {response_status}")
            print(f"Metadata: {metadata}")
            print("Connection closed\n")

            # Logging to server.log
            with open("server.log", "a") as log_file:
                log_file.write(f"{current_timestamp}\nConnection from {addr}\n")
                log_file.write(f"Full request:\n{request}")
                log_file.write(f"Response: {response_status}\n")
                log_file.write(f"Metadata: {metadata}\n")
                log_file.write("Connection closed\n")
                log_file.write("--------------------\n\n")

            # Sending response and closing connection
            conn.sendall(response)
            conn.close()


if __name__ == "__main__":
    server_root = os.path.abspath(".")  # or specify another directory
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 28333
    start_server(server_root, port)
