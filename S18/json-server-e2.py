import http.server
import socketserver
from pathlib import Path

PORT = 8000

class MyHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/listusers":
            try:
                # Leer archivo JSON
                json_data = Path("people-3.json").read_text()

                # Enviar respuesta
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()

                self.wfile.write(json_data.encode())

            except FileNotFoundError:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b"File not found")

        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not found")


# Ejecutar servidor
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()