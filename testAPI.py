import requests

res = requests.get(url="http://82.165.34.79/get")

print(res.content)