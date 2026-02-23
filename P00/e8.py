from Seq0 import most_frequent_base
Folder = "../Sequences/"
genes = ["U5", "ADA", "FRAT1", "FXN"]

print("------ | Exercise 8 | -----")

for gen in genes:
    filename = Folder + gen + ".txt"

    with open(filename, "r") as file:
        sequence = file.read().strip()

    result = most_frequent_base(sequence)
    print(f"Gene {gen}: Most frequent Base: {result}")