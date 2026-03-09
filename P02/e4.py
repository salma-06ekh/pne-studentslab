from Client0 import Client
from Seq01 import Seq

PRACTICE = 2
EXERCISE = 4

IP = "192.168.1.45" # your IP address
PORT = 8080

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
print(f"Connection to SERVER at {IP}, PORT: {PORT}")

c = Client(IP, PORT)
print("U5 Seq created")

s = Seq("U5.txt")
msg = "Sending U5  Gene to the server..."
print("To Server:")

gene = str(s)

print("To Server:", gene)

response = c.talk(gene)

print("From Server:")
print(response)





