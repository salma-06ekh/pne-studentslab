from Seq1 import Seq
print("-----| Practice 1, Exercise 10 |-----")

genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

for gene in genes:
    filename = gene + ".txt"

    with open(filename, "r") as f:
        sequence = ""
        for line in f:
            if not line.startswith(">"):
                sequence += line.strip()

    seq_obj = Seq(sequence)
    most_frq = seq_obj.most_freq_base()

    print(f"Gene {gene}: Most frequent Base: {most_frq}")
