def seq_ping():
    print("OK")

def seq_read_fasta(filename):
    sequence = " "

    with open(filename, "r") as file:
        for line in file:
            if line.startswith(">"):
                continue
            sequence += line.strip()
    return sequence

def seq_len(seq):
    return len(seq)

def seq_count_base(seq, base):
    count = 0
    for i in seq:
        if base == i:
            count += 1
    return count


def seq_count(seq):
    d = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for base in seq:
        if base in d:
            d[base] += 1

    return d

def seq_reverse(seq, n):
    f = seq[:n]
    rev = f[::-1]
    return rev

def seq_complement(seq):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    comp_seq = ""
    for base in seq:
        if base in complement:
            comp_seq += complement[base]
    return comp_seq


def most_frequent_base(sequence):
    max_count = 0
    most_frequent = ""
    for base in sequence:
        count = sequence.count(base)
        if count > max_count:
            max_count = count
            most_frequent = base
    return most_frequent