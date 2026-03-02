class Seq:
    def __init__(self, sequence):
        self.sequence = sequence
def print_seq(seq_list):
    for i, s in enumerate(seq_list):
        length = len(s.sequence)
        print(f"Sequence{i}: (Length: {length}) {s.sequence}")


def generate_seqs(pattern, number):
    result = []
    for i in range(1, number + 1):
        new_string = pattern * i
        result.append(Seq(new_string))
    return result

seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print("List 1:")
print_seq(seq_list1)

print()
print("List 2:")
print_seq(seq_list2)