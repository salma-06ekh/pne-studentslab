import http.server
import socketserver
from pathlib import Path

PORT = 8081

socketserver.TCPServer.allow_reuse_address = True


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        print("DEBUG PATH =", self.path)

        files = {
            "/": "html/index.html",
            "/index.html": "html/index.html",
            "/info/A": "html/info/A.html",
            "/info/C": "html/info/C.html",
            "/info/G": "html/info/G.html",
            "/info/T": "html/info/T.html",
        }

        try:
            if self.path in files:
                file_path = files[self.path]
                status = 200

            else:
                file_path = "html/error.html"
                status = 404
            print("Trying File:", file_path)
            content = Path(file_path).read_bytes()

            self.send_response(status)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(content)

        except FileNotFoundError:

            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"Error: file not found")


Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped by the user")
        httpd.server_close()