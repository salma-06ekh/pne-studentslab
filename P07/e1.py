import http.client
import json

SERVER = 'rest.ensembl.org'
ENDPOINT = '/info/ping'
PARAMS = '?content-type=application/json'
URL = SERVER + ENDPOINT + PARAMS

print()
print(f"Server: {SERVER}")
print(f"URL: {URL}")

conn = http.client.HTTPConnection(SERVER)

conn.request("GET", ENDPOINT + PARAMS)

response = conn.getresponse()

print(f"Response received: {response.status} {response.reason}")

data = response.read()

response = json.loads(data.decode("utf-8"))

if response.get("ping") == 1:
    print("PING OK! The database is running!")
else:
    print("PING ERROR! The database is NOT running!")

conn.close()