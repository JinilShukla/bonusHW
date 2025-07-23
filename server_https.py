# server.py
from http.server import BaseHTTPRequestHandler, HTTPServer
import ssl

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        print("Received POST:", post_data.decode())
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Login received')

# Create HTTP server
httpd = HTTPServer(('localhost', 8443), SimpleHTTPRequestHandler)

# Create SSL context (modern approach)
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile='cert.pem', keyfile='key.pem')

# Wrap the server's socket with SSL
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print("HTTPS server running at https://localhost:8443")
httpd.serve_forever()