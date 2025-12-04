#!/usr/bin/python3
"""
A simple HTTP server implementation using Python's http.server module.
This server handles GET requests for multiple endpoints and serves JSON data.
"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """Handler for HTTP GET requests."""
    
    def do_GET(self):
        """Handle GET requests for different endpoints."""
        if self.path == "/":
            # Root endpoint - returns simple text message
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
            
        elif self.path == "/data":
            # Data endpoint - returns JSON data
            content = {"name": "Holberton", "mission": "School"}
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(content).encode())
            
        elif self.path == "/status":
            # Status endpoint - returns API status
            content = {"status": "OK"}
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(content).encode())
            
        else:
            # Undefined endpoint - returns 404 error
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


if __name__ == "__main__":
    port = 8000
    server = HTTPServer(("0.0.0.0", port), SimpleHTTPRequestHandler)
    print(f"Starting server on port {port}...")
    print(f"http://localhost:{port}")
    server.serve_forever()
