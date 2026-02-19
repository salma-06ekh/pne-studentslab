def dnacount(dna):
    a_count = 0
    g_count = 0
    t_count = 0
    c_count = 0

    for base in dna:
        if base == "A":
            a_count += 1
        elif base == "G":
            g_count += 1
        elif base == "C":
            c_count += 1
        elif base == "T":
            t_count += 1

    print("Total length: ", len(dna))
    print("A: ", a_count)
    print("G: ", g_count)
    print("c: ", c_count)
    print("T: ", t_count)

sequence = input("Enter a dna sequence: ")
dnacount(sequence)



