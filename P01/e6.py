from Seq1 import Seq

print("-----| Practice 1, Exercise 6 |-----")


s1 = Seq()
s2 = Seq("TATAC")
s3 = Seq("Invalid sequence")

print(f"Sequence 1: (Length: {len(s1)}) {s1}")
print(f"  Bases: {s1.count()}")

print(f"Sequence 2: (Length: {len(s2)}) {s2}")
print(f"   Bases: {s2.count()}")

print(f"Sequence 3: (Length: {len(s3)}) {s3}")
print(f"   Bases: {s3.count()}")

