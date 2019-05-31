import requests

res = requests.get('https://digitalinnovation.one/blog/')
res.encoding = "utf-8"

print(res.text)