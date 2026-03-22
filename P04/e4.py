import socket
import termcolor


# -- Server network parameters
IP = "127.0.0.1"
PORT = 8080


def process_client(s):
    # -- Receive the request message
    req_raw = s.recv(2000)
    req = req_raw.decode()

    print("Message FROM CLIENT: ")

    # -- Split the request messages into lines
    lines = req.split('\r\n')

    # -- The request line is the first
    req_line = lines[0]
    parts = req_line.split(" ")
    print("Request line: ", req_line)
    termcolor.cprint(req_line, "green")
    resource = parts[1]

    # -- Let's start with the body
    if resource == "/info/A":
        f = open("html/info/A.html")
        body = f.read()
        f.close()
    elif resource == "/info/C":
        f = open("html/info/C.html")
        body = f.read()
        f.close()
    elif resource == "/info/G":
        f = open("html/info/G.html")
        body = f.read()
        f.close()
    elif resource == "/info/T":
        f = open("html/info/T.html")
        body = f.read()
        f.close()
    else:
        body = ""

    # -- Status line: We respond that everything is ok (200 code)
    status_line = "HTTP/1.1 200 OK\r\n"

    # -- Add the Content-Type header
    header = "Content-Type: text/html\r\n\r\n\r\n\r\n"

    # -- Add the Content-Length
    header += f"Content-Length: {len(body)}\r\n"

    # -- Build the message by joining together all the parts
    response_msg = status_line + header + "\r\n" + body
    s.send(response_msg.encode())


# -------------- MAIN PROGRAM
# ------ Configure the server
# -- Listening socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Setup up the socket's IP and PORT
ls.bind((IP, PORT))

# -- Become a listening socket
ls.listen()

print("Echo server configured!")

# --- MAIN LOOP
while True:
    print("Waiting for clients....")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server stopped!")
        ls.close()
        exit()
    else:

        # Service the client
        process_client(cs)

        # -- Close the socket
        cs.close()