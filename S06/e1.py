class Seq:
    def __init__(self, sequence):
        print("New sequence created!")
        valid_bases = {'A', 'C', 'G', 'T'}

        for base in sequence:
            if base not in valid_bases:
                self.sequence = "ERROR"
                print("ERROR!!")
                return
        self.sequence = sequence

s1 = Seq("ACCTGC")
S2 = Seq("ACCTGX")

print(f"Sequence 1: {s1.sequence}")
print(f"Sequence 2: {S2.sequence}")