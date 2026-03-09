import socket

# SERVER IP, PORT
PORT = 65432
IP = "127.0.0.1" # depends on the computer the server is running

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP, PORT))
s.listen(1)

print(f"SERVER: waiting for {PORT}...")
conn, dir = s.accept()
print(f"¡CONNECTED!: {dir}")

message = conn.recv(1024).decode()
print(f"Message received: {message}")

conn.send("Server received".encode())
conn.close()