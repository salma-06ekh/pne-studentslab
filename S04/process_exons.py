from pathlib import Path

def get_exons_from_file(filename):
    exons = []
    path = Path(filename)
    seq = ""
    for line in path.read_text().splitlines():
        if line.startswith(">"):
            if seq:
                exons.append(seq)
                seq = ""
        else:
            seq += line.strip()
    if seq:
        exons.append(seq)
    return exons
apoe_exons = get_exons_from_file("Sequences/APOE_EXONS.txt")
print(apoe_exons)
