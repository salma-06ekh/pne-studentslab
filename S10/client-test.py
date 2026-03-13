from Client0 import Client
from termcolor import colored

SERVER_IP = "127.0.0.1"
SERVER_PORT = 8080

for i in range(5):
    c = Client(SERVER_IP, SERVER_PORT)
    message = f"message {i}"

    print(f"Sending: {message}")

    response = c.talk(message)
    print(f"Response from server: {response}")