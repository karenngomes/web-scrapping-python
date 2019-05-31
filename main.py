import requests
from bs4 import BeautifulSoup

res = requests.get('https://digitalinnovation.one/blog/')
res.encoding = "utf-8"

soup = BeautifulSoup(res.text, 'html.parser')

all_posts = soup.find_all(class_='post')
print(all_posts)