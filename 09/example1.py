import requests
import json

cep = "04578910"

#request CEP
response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")

if response.status_code == 200: #get status code
    
    data_json = json.loads(response.content) #converting JSON to a python object

    print(f"Loading info CEP: {cep}...", end="\n\n")

    for k, v in data_json.items():
        print(f"{k}: {v}")
else:
    print(f"Error to make request, code error: {response.status_code}")