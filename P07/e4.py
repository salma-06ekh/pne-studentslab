import http.client
import json

genes = {
    "FRAT1": "ENSG00000165879",
    "ADA": "ENSG00000196839",
    "FXN": "ENSG00000165060",
    "RNU6-269P": "ENSG00000212385",
    "MIR633": "ENSG00000207716",
    "TTTY4C": "ENSG00000229807",
    "RBMY2YP": "ENSG00000214728",
    "FGFR3": "ENSG00000068078",
    "KDR": "ENSG00000128052",
    "ANK2": "ENSG00000145362"
}

gene_name = input("Write the gene name: ")

gene_id = genes.get(gene_name)

if not gene_id:
    print("Gene not found!")
    exit()

SERVER = "rest.ensembl.org"
ENDPOINT = f"/sequence/id/{gene_id}"
PARAMS = "?content-type=application/json"

conn = http.client.HTTPConnection(SERVER)
conn.request("GET", ENDPOINT + PARAMS)

response = conn.getresponse()
data = response.read()
response = json.loads(data.decode("utf-8"))

seq = response.get("seq")
desc = response.get("desc")

total = len(seq)

a = seq.count("A")
c = seq.count("C")
g = seq.count("G")
t = seq.count("T")

pa = a / total * 100
pc = c / total * 100
pg = g / total * 100
pt = t / total * 100

bases = {"A": a, "C": c, "G": g, "T": t}
most_freq = max(bases, key=bases.get)

print()
print(f"Description: {desc}")
print("New sequence created!")

print(f"Total length: {total}")
print(f"A: {a} ({pa:.1f}%)")
print(f"C: {c} ({pc:.1f}%)")
print(f"G: {g} ({pg:.1f}%)")
print(f"T: {t} ({pt:.1f}%)")
print(f"Most frequent bases: {most_freq}")

conn.close()