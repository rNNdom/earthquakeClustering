import http.server
import socketserver
import webbrowser
import time
import os

class CORSRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        return super().end_headers()

    def do_GET(self):
        # Print the requested file path
        print(f"File path: {self.path}")
        # Check if the file exists
        file_exists = os.path.isfile(self.path[1:])
        print(f"File exists: {file_exists}")
        return super().do_GET()

PORT = 8000

# Print the current working directory
print(f"Current working directory: {os.getcwd()}")

with socketserver.TCPServer(("", PORT), CORSRequestHandler) as httpd:
    print("serving at port", PORT)
    # Wait for the server to initialize
    time.sleep(1)
    # Open the web page
    webbrowser.open('http://localhost:8000/map3.html')
    httpd.serve_forever()

# Fn + F5 to run, Shift + Fn + F5 to stop