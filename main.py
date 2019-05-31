import requests
import json
from bs4 import BeautifulSoup

res = requests.get('https://digitalinnovation.one/blog/')
res.encoding = "utf-8"

soup = BeautifulSoup(res.text, 'html.parser')

posts = soup.find_all(class_='post')
all_posts = []

for post in posts:
    info = post.find(class_='post-content')
    title = info.h2.text
    preview = info.p.text
    author = info.find(class_='post-author').text[5:]
    time = info.footer.time['datetime']
    img = post.find(class_='wp-post-image')['src']
    all_posts.append({'title': title, 'preview': preview,
                      'author': author, 'time': time, 'img': img})

with open('posts.json', 'w') as json_file:
    json.dump(all_posts, json_file, indent=3, ensure_ascii=False)
