from Seq0 import seq_reverse
Folder = "../Sequences/"
gen = "U5"
filename = Folder + gen + ".txt"

with open(filename, "r") as file:
    file.readline()
    sequence = file.read().replace("\n", " ")

f = sequence[:20]
reverse = seq_reverse(sequence, 20)

print("------ | Exercise 6 | ------")
print("Gen: ", gen)
print("Fragment: ", f)
print("Reverse: ", reverse)
