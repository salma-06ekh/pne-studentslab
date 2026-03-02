class Seq:
    """A class for representing sequences"""

    def __init__(self, seq):
        self.seq = seq

    def __len__(self):
        return len(self.seq)

    def __str__(self):
        return self.seq

print("Testing....")
