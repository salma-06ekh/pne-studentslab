class Seq:
    def __init__(self, sequences):
        self.sequence = sequences


def print_seqs(seq_list):
    for i, s in enumerate(seq_list):
        length = len(s.sequence)
        print(f"Sequence{i}: (Length: {length}) {s.sequence}")

seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
print_seqs(seq_list)
