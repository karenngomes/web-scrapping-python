import requests
from bs4 import BeautifulSoup

res = requests.get('https://digitalinnovation.one/blog/')
res.encoding = "utf-8"

soup = BeautifulSoup(res.text, 'html.parser')

posts = soup.find_all(class_='post')
all_posts = []

for post in posts:
    info = post.find(class_='post-content')
    title = info.h2.text
    print(title)