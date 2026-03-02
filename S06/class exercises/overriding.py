from S06.Seq01 import Seq
class Gene(Seq):
    """This class is derived from the Seq Class
       All the objects of class Gene will inherit
       the methods from the Seq class
    """
    def __init__(self, strbases, name=""):
        super().__init__(strbases)
        self.name = name
        self.strbases = strbases
        print("New gene created")

    def __str__(self):
        """Print the Gene name along with the sequence"""
        return self.name + "-" + self.strbases

s1 = Seq("AGTACACTGGT")
g = Gene("CGTAAC", "FRAT1")

print(f"Sequence 1: {s1}")
print(f"Gene: {g}")
