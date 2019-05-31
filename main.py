import requests

res = requests.get('http://digitalinnovation.one/blog/')
res.encoding = "utf-8"

print(res)