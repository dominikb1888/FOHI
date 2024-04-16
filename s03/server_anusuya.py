import os
import mimetypes
from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Read the full request header
        header_data = self.rfile.read().decode("ISO-8859-1")

        # Split the header data into individual lines
        header_lines = header_data.split("\r\n")

        # Get the first line (GET line)
        get_line = header_lines[0]

        # Split the GET line into its three parts
        _, _, _ = get_line.split()

        # Use the path for further processing
        file_name = os.path.basename("/Users/anusuyakugavarathan/Programming/HTTP_client_and_server/main.rs".strip('/'))

        # Read the data from the named file
        try:
            with open(file_name, 'rb') as file:
                file_data = file.read()
        except FileNotFoundError:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'File not found :) ')
            return

        # Determine the type of data in the file
        content_type, _ = mimetypes.guess_type(file_name)
        if content_type is None:
            content_type = 'application/octet-stream'

        # Build the HTTP response packet
        self.send_response(200)
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', str(len(file_data)))
        self.send_header('Connection', 'close')
        self.end_headers()

        # Send the file data in the payload
        self.wfile.write(file_data)

def run_server(port):
    server_address = ('', port)
    httpd = HTTPServer(server_address, MyHTTPRequestHandler)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server(33490)
