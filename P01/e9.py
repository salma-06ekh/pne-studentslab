from Seq1 import Seq
print("-----| Practice 1, Exercise 9 |-----")

s = Seq()
print("NULL Sequence created")

s.read_fasta("U5.txt")

print(f"Sequence : (Length: {len(s)}) {s}")
print(f"  Bases: {s.count()}")
print(f"  Reverse: {s.reverse()}")
print(f"  Complement: {s.complement()}")

