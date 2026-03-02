from S06.Seq01 import Seq
class Gene(Seq):
    """This class is derived from the Seq Class
       All the objects of class Gene will inherit
       the methods from the Seq class
    """
    def __init__(self, strbases, name=""):
        super().__init__(strbases)
        self.name = name
        print("New gene created")

s1 = Seq("AGTACACTGGT")
g = Gene("CGTAAC", "FRAT1")

print(f"Sequence 1: {s1}")
print(f"Gene: {g}")
