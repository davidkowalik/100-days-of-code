import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇


response = requests.get(URL)
web_data = response.text

soup = BeautifulSoup(web_data, 'html.parser')
headings_list = soup.find_all(name='h3', class_='title')
titles_list = [item.getText() for item in headings_list]
titles_list.reverse()


# #prepare text in str and write to file at once ------------------------
# movies_to_watch = ""
# for item in titles_list:
#     movies_to_watch = movies_to_watch + f"{item}\n"

# with open("movies.txt", 'w', encoding="utf-8") as file:
#     file.write(movies_to_watch)


# #write to file line by line in a loop directly form titles list------------------------
with open("movies.txt", 'a', encoding="utf-8") as file:
    for item in titles_list:
        file.write(f"{item}\n")