import json
import termcolor
from pathlib import Path

# Read JSON file
jsonstring = Path("people-3.json").read_text()

# Convert to Python list
people = json.loads(jsonstring)

# Print total number of people
print()
print("Total people in the database:", len(people))
print()

# Loop through all people
for person in people:
    termcolor.cprint("Name: ", 'green', end="")
    print(person['Firstname'], person['Lastname'])

    termcolor.cprint("Age: ", 'green', end="")
    print(person['age'])

    phoneNumbers = person['phoneNumber']

    termcolor.cprint("Phone numbers: ", 'green', end='')
    print(len(phoneNumbers))

    # Loop phone numbers
    for i, num in enumerate(phoneNumbers):
        termcolor.cprint("  Phone " + str(i) + ": ", 'blue')

        termcolor.cprint("    Type: ", 'red', end='')
        print(num['type'])

        termcolor.cprint("    Number: ", 'red', end='')
        print(num['number'])

    print()