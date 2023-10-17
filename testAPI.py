import requests

res = requests.get(url="http://127.0.0.1:5000/get")

print(res.content)