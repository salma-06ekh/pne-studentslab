from pathlib import Path
FILENAME = Path("Sequences/ADA_genes.txt")

sequence = FILENAME.read_text().split('\n')

line_sequence = sequence[1:]

total_bases = 0
for line in line_sequence:
    total_bases = total_bases + len(line)

print(total_bases)