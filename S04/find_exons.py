from pathlib import Path
MAX_COORD = 44652852

gene_file = Path("Sequences/ADA_genes.txt")
exons_file = Path("Sequences/ADA_EXONS.txt")

def read_fasta(path):
    sequence = ""
    with path.open() as file:
        for line in file:
            if not line.startswith(">"):
                sequence += line.strip()
    return sequence

def read_fasta_m(path):
    seq = []
    n_seq = ""

    with path.open() as file:
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                if n_seq:
                    seq.append(n_seq)
            else:
                n_seq += line
        if n_seq:
            seq.append(n_seq)
    return seq

def reverse_coordinates(index, length):
    start = MAX_COORD - index
    end = start - length + 1
    return end, start

gene_sequence = read_fasta(gene_file)
exons = read_fasta_m(exons_file)

print(f"{'Exon':<5} | {'Long.':<5} | {'Start':<10} | {'End':<10}")
print("----------------------------------")

for i , exon in enumerate(exons, start=1):
    index = gene_sequence.find(exon)

    if index == -1:
        print(f"Exon{i} not found")
        continue
    length = len(exon)

    start, end = reverse_coordinates(index, length)
    print(f"{i:<5} | {length:<5} | {start:<10} | {end:<10}")
