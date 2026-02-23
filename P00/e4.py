from Seq0 import seq_count_base

Folder = "../Sequences/"
genes = ["U5", "ADA", "FRAT1", "FXN"]
bases = ["A", "C", "G", "T"]

for gen in genes:
    filename = Folder + gen + ".txt"

    with open(filename, "r") as file:
        sequence = file.read().strip()
    print("Gen:", gen)

    for base in bases:
        count = seq_count_base(sequence, base)
        print(base, ":", count)

    print()