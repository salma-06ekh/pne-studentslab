from S06.Seq01 import Seq
class Gene(Seq):
    """This class is derived from the Seq Class
    All the objects of class Gene will inherit
    the methods from the Seq class
    """
    pass

s1 = Seq("AGTACACTGGT")
g = Gene("CGTAAC")

print(f"Sequence 1: {s1}")
print(f"  Length: {len(s1)}")
print(f"Gene: {g}")
print(f"  Length: {len(g)}")
