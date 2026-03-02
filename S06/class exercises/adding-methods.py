class Seq:
    """A class to represent a sequence"""
    def __init__(self, strbases):
        self.strbases = strbases
        print("New sequence created!")


    def __str__(self):
        """Method called when the object is being printed"""
        return self.strbases
    def __len__(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)

s1 = Seq("AGTACACTGGT")
s2 = Seq("CGTAAC")

print(f"Sequence 1: {s1}")
print(f"   Length: {len(s1)}")
print(f"Sequence 2: {s2}")
print(f"   Length: {len(s2)}")