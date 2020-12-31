import requests
import json

#CONSULTANDO CEP
cep = "04578910"

response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")

#CONVERTENDO O JSON PARA UM OBJETO PYTHON
data_json = json.loads(response.content)

print("Carregando infos sobre o CEP: {cep}...", end="\n\n")

for k, v in data_json.items():
    print(f"{k}: {v}")