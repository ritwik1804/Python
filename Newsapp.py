import json

import requests

query = input("what type of news are you intrested in")
url = f"https://newsapi.org/v2/everything?q={query}&from=2024-10-22&sortBy=publishedAt&apiKey=c6ce3bbed7e44a349894073047bdf8a6"
r = requests.get(url)
news = json.loads(r.text)
print(news, type(news))

for article in news["articles"]:
    print(article["title"])
    print(article["description"])
