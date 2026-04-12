import http.server
import socketserver
from pathlib import Path

PORT = 8080

socketserver.TCPServer.allow_reuse_address = True


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        print("Request:", self.requestline)
        print("  Path: " + self.path)

        file_path = self.path.lstrip("/")

        if file_path == "":
            file_path = "index.html"

        try:
            content = Path(file_path).read_bytes()

            self.send_response(200)
            self.send_header("Content type", "text/html")
            self.end_headers()
            self.wfile.write(content)

        except FileNotFoundError:
            try:
                error_content = Path("error.html").read_bytes()
                self.send_response(404)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(error_content)

            except FileNotFoundError:
                self.send_response(404)
                self.end_headers()
                self.send_header("Content-type", "text/html")


Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped by the user")
        httpd.server_close()