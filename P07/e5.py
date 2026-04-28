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
SERVER = "rest.ensembl.org"

for gene_name, gene_id in genes.items():
    print("\n-------------------------------")

    ENDPOINT = f"/sequence/id/{gene_id}"
    PARAMS = "?content-type=application/json"
    URL = SERVER + ENDPOINT + PARAMS

    print(f"Server: {SERVER}")
    print(f"URL: {URL}")

    conn = http.client.HTTPConnection(SERVER)
    try:
        conn.request("GET", ENDPOINT + PARAMS)
    except ConnectionRefusedError:
        print("ERROr! Cannot connect to the server")
        continue
    response = conn.getresponse()
    print(f"Response received: {response.status} {response.reason}")

    data = response.read()
    response = json.loads(data.decode("utf-8"))

    seq = response.get("seq")
    desc = response.get("desc")

    if not seq:
        print("Error: sequence not available for this gene")
        conn.close()
        continue

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
    print(f"Gene: {gene_name}")
    print(f"Description: {desc}")
    print("New sequence created!")

    print(f"Total length: {total}")
    print(f"A: {a} ({pa:.1f}%)")
    print(f"C: {c} ({pc:.1f}%)")
    print(f"G: {g} ({pg:.1f}%)")
    print(f"T: {t} ({pt:.1f}%)")
    print(f"Most frequent bases: {most_freq}")

    conn.close()