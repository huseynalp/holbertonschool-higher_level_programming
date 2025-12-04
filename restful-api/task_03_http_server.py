#!/usr/bin/python3
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        """Handle GET requests."""
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            content = {"name": "Holberton", "mission": "School"}
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(content).encode())

        elif self.path == "/status":
            content = {"status": "OK"}
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(content).encode())

        else:
            # REQUIRED BEHAVIOR FOR TEST 4
            self.send_response(404)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            content = {"error": "Endpoint not found"}
            self.wfile.write(json.dumps(content).encode())


if __name__ == "__main__":
    port = 8000
    server = HTTPServer(("0.0.0.0", port), SimpleHTTPRequestHandler)
    print(f"Starting server on port {port}...")
    print(f"http://localhost:{port}")
    server.serve_forever()
