from bs4 import BeautifulSoup
import requests

# with open("bs4-start/website.html") as page:
#     soup = BeautifulSoup(page, 'html.parser')

# print(soup.get_text())

# ---------------------------------------------------------------------------


response = requests.get("https://news.ycombinator.com/newest")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')

test = soup.select_one('.titleline a').getText()

print(test)