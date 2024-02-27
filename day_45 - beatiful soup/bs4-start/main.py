from bs4 import BeautifulSoup
import requests

# with open("bs4-start/website.html") as page:
#     soup = BeautifulSoup(page, 'html.parser')

# print(soup.get_text())

# ---------------------------------------------------------------------------


response = requests.get("https://news.ycombinator.com/newest")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')

article_tag = soup.select_one('.titleline a')

article_tag1 = soup.find(name = 'span', class_='titleline')

print(article_tag1)

# article_score = soup.select_one('span .score').getText()

# print(article_score)