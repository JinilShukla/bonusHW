# server.py
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        print("Received POST:", post_data.decode())
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Login received')

httpd = HTTPServer(('localhost', 8080), SimpleHTTPRequestHandler)
print("Server running on http://localhost:8080")
httpd.serve_forever()

