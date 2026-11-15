#!/usr/bin/env python3
import http.server
import socketserver
import webbrowser
import sys
import os

PORT = 8080

os.chdir(os.path.dirname(os.path.abspath(__file__)))

Handler = http.server.SimpleHTTPRequestHandler

class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

try:
    with ReusableTCPServer(("", PORT), Handler) as httpd:
        print(f"=======================================================")
        print(f"  247 Free Poker (Texas Hold'em) Local Server")
        print(f"  Open in your browser: http://localhost:{PORT}")
        print(f"=======================================================")
        print("Press Ctrl+C to stop.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server.")
except Exception as e:
    print(f"Error starting server on port {PORT}: {e}")
    sys.exit(1)
