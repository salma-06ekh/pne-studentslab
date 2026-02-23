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