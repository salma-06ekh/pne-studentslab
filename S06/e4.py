from termcolor import colored
class Seq:
    def __init__(self, sequence):
        print("New sequence created!!")
        self.sequence = sequence

def print_seq(seq_list, color):
    for i, s in enumerate(seq_list):
        length = len(s.sequence)
        output = f"Sequence{i}: (Length: {length}) {s.sequence}"
        print(colored(output, color))

def generate_seqs(pattern, number):
    result = []
    for i in range(1, number + 1):
        result.append(Seq(pattern * i))
    return result

seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print("List 1:")
print_seq(seq_list1, "blue")

print()
print("List 2:")
print_seq(seq_list2, "green")