from Client0 import Client

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "192.168.1.45" # your IP address
PORT = 8080

print(f"Connection to SERVER at{IP}, PORT:{PORT}")

c = Client(IP, PORT)

with open("Sequences/FRAT1.txt", "r") as file:
    lines = file.readlines()
    gene = file.read().join(lines[1:]).replace("\n", "")
print("Gene FRAT1:", gene)

for i in range(5):
    fragment = gene[i*10:(i+1)*10]
    print(f"Fragment {i+1}: {fragment}")
