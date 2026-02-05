"""
Simple HTTP server for the frontend
Run this to serve the frontend properly
"""
import http.server
import socketserver
import os

PORT = 3000
DIRECTORY = "frontend"

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
    print(f"✅ Frontend server running at http://localhost:{PORT}")
    print(f"📁 Serving directory: {DIRECTORY}")
    print(f"🌐 Open: http://localhost:{PORT}/index.html")
    print("\nPress Ctrl+C to stop")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\n👋 Server stopped")
