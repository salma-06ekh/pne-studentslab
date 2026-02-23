import Seq0
Folder = "../sequences/"

genes = ["U5", "ADA", "FRAT1", "FXN"]

print("-----| Exercise 3 |-----")

for gen in genes:
    filename = Folder + gen + ".txt"
    seq = Seq0.seq_read_fasta(filename)
    length = Seq0.seq_len(seq)

    print("Gen", gen, "-> Length:", length)