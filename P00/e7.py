from Seq0 import seq_complement

Folder = "../Sequences/"
gen = "U5"
filename = Folder + gen + ".txt"

with open(filename, "r") as file:
    file.readline()
    sequence = file.read().replace("\n", " ")

frag = sequence[:20]
complement = seq_complement(frag)

print("------ | Exercise 7 | ------")
print("Gen U5:")
print("Frag: ", frag)
print("Complement: ", complement)