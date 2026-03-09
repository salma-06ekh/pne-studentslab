from Client0 import Client

PRACTICE = 2
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

SERVER1_IP = "192.168.1.45" # your IP address
SERVER1_PORT = 8080
SERVER2_IP = "192.168.1.45"
SERVER2_PORT = 8081

with open("Sequences/FRAT1.txt", "r") as file:
    lines = file.readlines()
    gene = file.read().join(lines[1:]).replace("\n", "")
print("Gene FRAT1:", gene)

fragment = list(gene[:10])

for i, base in enumerate(fragment):
    fragment_number = i + 1
    message = f"Fragment {fragment_number}: {base}"
    print(message)
    if fragment_number % 2 == 1:
        IP = SERVER1_IP
        PORT = SERVER1_PORT
    else:
        IP = SERVER2_IP
        PORT = SERVER2_PORT
    print(f"Connection to SERVER at {IP}, PORT:{PORT}")
    c = Client(IP, PORT)
    c.talk(message)