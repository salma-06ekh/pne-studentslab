from pathlib import Path

FILENAME = Path("Sequences/RNU6_269P.TXT")

head = FILENAME.read_text().split('\n')[0]
print(head)