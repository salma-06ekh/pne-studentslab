def count_bases(content):
    total = 0
    a = 0
    c = 0
    g = 0
    t = 0

    with open(content, "r") as file:
        for line in file:
            line = line.strip()
            for base in line:
                total += 1
                if base == "A":
                    a += 1
                elif base == "C":
                    c += 1
                elif base == "G":
                    g += 1
                elif base == "T":
                    t += 1

    return total, a, c, g, t

def main():
    total, a, c, g, t = count_bases("dna.txt")

    print("Total of bases: ", total)
    print("A:", a)
    print("C:", c)
    print("G:", g)
    print("T:", t)

main()
