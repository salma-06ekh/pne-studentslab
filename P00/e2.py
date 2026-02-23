import Seq0
Folder = "../sequences/"
File = "U5.txt"

full_path = Folder + File
print("DNA file: ", File)

sequence = Seq0.seq_read_fasta(full_path)
print("The first 20 bases are: ")
print(sequence[0:20])