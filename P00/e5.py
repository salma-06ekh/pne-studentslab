from Seq0 import seq_count

Folder = "../Sequences/"
genes = ["U5", "ADA", "FRAT1", "FXN"]
bases = ["A", "C", "G", "T"]

for gen in genes:
    filename = Folder + gen + ".txt"

    with open(filename, "r") as file:
        sequence = file.read().strip()

    counts = seq_count(sequence)
    print("Gen:", gen, ":", counts)