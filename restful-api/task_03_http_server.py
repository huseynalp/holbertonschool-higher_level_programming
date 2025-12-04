#!/usr/bin/python3
"""
Simple HTTP server using http.server module.

Endpoints:
    /           -> returns a simple text message
    /data       -> returns sample JSON data
    /status     -> returns API status "OK"
    undefined   -> returns 404 JSON error
"""

from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Custom handler for a simple HTTP API."""

    def log_message(self, format, *args):
        """Disable logging so test output is clean."""
        return

    def do_GET(self):
        """Handle GET requests for different endpoints."""
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            # Must match test EXACTLY (no spaces)
            self.wfile.write(b'{"name":"John","age":30,"city":"New York"}')

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            # Undefined endpoint → 404 with exact JSON
            self.send_response(404)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"error":"Endpoint not found"}')


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler):
    """Run the HTTP server on port 8000."""
    server_address = ("", 8000)
    httpd = server_class(server_address, handler_class)
    print("Starting server on port 8000...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
