class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases):
        self.strbases = strbases
        print("New sequence created!")

    def __str__(self):
        """Method called when the object is being printed"""
        return self.strbases

s1 = Seq("AGTACACTGGT")
s2 = Seq("CGTAAC")

print(f"Sequences 1: {s1}")
print(f"Sequences 2: {s2}")
print("Testing....")