from pathlib import Path

file_contents = Path('Sequences/RNU6_269P.TXT').read_text()
print(file_contents)