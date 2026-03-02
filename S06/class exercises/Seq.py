def seq_reverse(seq):
    return seq[::-1]

def seq_complement(seq):
    complement = {"A":"T", "T":"A", "C":"G", "G":"C"}
    return "".join(complement[b] for b in seq)

def seq_len(seq):
    return len(seq)

def seq_count_base(seq, base):
    return seq.count(base)