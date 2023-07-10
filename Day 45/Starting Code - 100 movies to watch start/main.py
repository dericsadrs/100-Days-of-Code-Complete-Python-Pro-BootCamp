
import requests, lxml
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "lxml")

all_movies = soup.find_all(name="h3", class_="title")

movies_to_watch = [movie.getText() for movie in all_movies]
print(movies_to_watch[::-1])

with open("movies.txt", mode="w", encoding="utf-8") as file:
    for movie in movies_to_watch:
        file.write(f"{movie}\n")
