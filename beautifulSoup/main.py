from bs4 import BeautifulSoup
import requests
# with open("website.html", encoding="utf-8") as file:
#     contents = file.read()
# soup = BeautifulSoup(contents, "html.parser")
# name = soup.select_one(selector="#name")
# print(name)

response = requests.get("https://news.ycombinator.com/news")
contents = response.text
soup = BeautifulSoup(contents, "html.parser")
articles = soup.select(selector=".titleline > a")
article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)
print(article_texts[largest_index])
print(article_links[largest_index])
