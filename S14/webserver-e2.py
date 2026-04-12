import http.server
import socketserver

PORT = 8080

socketserver.TCPServer.allow_reuse_address = True


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        print("Request:", self.requestline)
        print("  Path: " + self.path)

        if self.path == "/" or self.path == "/index.html":

            file = open("index.html", "rb")
            content = file.read()
            file.close()

            self.send_response(200)
            self.send_header("Content type", "text/html")
            self.end_headers()
            self.wfile.write(content)

        else:
            file = open("error.html", "rb")
            content = file.read()
            file.close()

            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(content)


Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped by the user")
        httpd.server_close()