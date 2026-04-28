import http.client
import json

SERVER = "rest.ensembl.org"
GENE_ID = "ENSG00000207716"

ENDPOINT = f"/sequence/id/{GENE_ID}"
PARAMS = "?content-type=application/json"

URL = SERVER + ENDPOINT + PARAMS

print(f"Server: {SERVER}")
print(f"URL: {URL}")

conn = http.client.HTTPSConnection(SERVER)
conn.request("GET", ENDPOINT + PARAMS)

response = conn.getresponse()
print(f"Response received: {response.status} {response.reason}")

data = response.read()
response = json.loads(data.decode("utf-8"))

print()
print("Gene: MIR633")
print(f"Description: {response.get('desc')}")
print(f"Bases: {response.get('seq')}")

conn.close()
