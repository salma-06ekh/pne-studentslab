class Seq:
    def __init__(self, sequence=""):
        self.sequence = sequence

    def __str__(self):
        if self.sequence =="":
            return "Empty sequence"
        return self.sequence

    def __len__(self):
        return len(self.sequence)

    def count(self):

        if self.sequence is None or self.sequence == "":
            return {}
        return{
        'A': self.sequence.count('A'),
        'T': self.sequence.count('T'),
        'C': self.sequence.count('C'),
        'G': self.sequence.count('G')
        }

    def reverse(self):
        if not self.sequence is None:
            return self.sequence[::-1]

        else:
            return ""

    def complement(self):
        comp_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        comp_seq = ""
        for base in self.sequence:
            if base in comp_dict:
                comp_seq += comp_dict[base]
            else:
                comp_seq += "N"
        return comp_seq


    def read_fasta(self, filename):
        self.sequence = ""
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith(">"):
                    self.sequence += line

    def most_freq_base(self):
        if self.sequence == "":
            return None

        counts = {}

        for base in self.sequence:
            if base in counts:
                counts[base] += 1
            else:
                counts[base] = 1

        return max(counts, key=counts.get)

