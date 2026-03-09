import socket

# SERVER IP, PORT
IP = "192.168.1.45" # depends on the computer the server is running
PORT = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((IP, PORT))
s.listen(1)

print(f"SERVER: waiting for {PORT}...")
while True:
    conn, dir = s.accept()
    print(f"¡CONNECTED!: {dir}")

    message = conn.recv(1024).decode()
    print(f"Message received: {message}")

    conn.send("Server received".encode())
    conn.close()