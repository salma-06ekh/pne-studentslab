import socket

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

PORT = 8080
IP = "127.0.0.1"

ls.bind((IP, PORT))
ls.listen()
print("The server is configured!")
connections = 0
clients = []

while True:
    print("Waiting for Clients to connect")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Client stopped")
        ls.close()
        exit()
    else:
        connections += 1
        print(f"Client connected: {connections}. Client IP, PORT: {client_ip_port}")
        clients.append(client_ip_port)

        msg_raw = cs.recv(2048)
        msg = msg_raw.decode()
        print(f"Message received: {msg}")
        response = "ECHO: " + msg
        cs.send(response.encode())
        cs.close()
        if connections == 5:
            print("Client connected", {connections}, ":")
            for client in clients:
                print(client)
            ls.close()
            print("Server finished.")
            break