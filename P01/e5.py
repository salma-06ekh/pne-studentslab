from Seq1 import Seq

print("-----| Practice 1, Exercise 5 |-----")


s1 = Seq()
s2 = Seq("TATAC")
s3 = Seq("Invalid sequence")

print(f"Sequence 1: (Length: {len(s1)}) {s1}")
print(f"   A: {s1.count_base('A')}, C: {s1.count_base('C')}, G: {s1.count_base('G')}, T: {s1.count_base('T')}")

print(f"Sequence 2: (Length: {len(s2)}) {s2}")
print(f"   A: {s2.count_base('A')}, C: {s2.count_base('C')}, G: {s2.count_base('G')}, T: {s2.count_base('T')}")

print(f"Sequence 3: (Length: {len(s3)}) {s3}")
print(f"   A: {s3.count_base('A')}, C: {s3.count_base('C')}, G: {s3.count_base('G')}, T: {s3.count_base('T')}")

