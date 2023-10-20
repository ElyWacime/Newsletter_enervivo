import requests

res = requests.post("https://api.enervivo.fr/get")
print(res.content)