from pathlib import Path

FILENAME = Path("Sequences/U5.txt")

body = FILENAME.read_text().split('\n')
for line in body[1:]:
    print(line)
