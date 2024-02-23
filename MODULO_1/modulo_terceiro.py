print ("\nImportação e uso de um módulo de terceiros")
import requests

url = "https://www.example.com"

response = requests.get(url)
"""
200 - tudo certo
404 - nao existe
500 - interal server error 
"""
print(f"Solicitação http para {url} retornou com status {response.status_code}")