import urllib.request
import json
import termcolor

# URL del servidor
url = "http://localhost:8000/listusers"

# Hacer petición
response = urllib.request.urlopen(url)

# Leer datos
data = response.read().decode()

# Convertir JSON a lista
people = json.loads(data)

# Mostrar número total
print("Total people:", len(people))
print()

# Recorrer personas
for person in people:
    termcolor.cprint("Name: ", 'green', end="")
    print(person['Firstname'], person['Lastname'])

    termcolor.cprint("Age: ", 'green', end="")
    print(person['age'])

    phones = person['phoneNumber']

    termcolor.cprint("Phones: ", 'green', end="")
    print(len(phones))

    for i, p in enumerate(phones):
        termcolor.cprint("  Phone " + str(i) + ": ", 'blue')

        termcolor.cprint("    Type: ", 'red', end="")
        print(p['type'])

        termcolor.cprint("    Number: ", 'red', end="")
        print(p['number'])

    print()