from bs4 import BeautifulSoup
import lxml

with open("website.html", "r", encoding="utf-8") as file:
    contents = file.read()
soup = BeautifulSoup(contents, "lxml")
print(soup.title.string)
# print(soup.title.prettify())
anchor_tags = soup.find_all(name="a")
#
# for tag in anchor_tags:
#     print(tag.get("href"))

# heading = soup.find(name="h1",id="name")


section_heading = soup.find(name="h3", class_="heading")
print(section_heading.get("class"))

name = soup.select_one(selector="#name")

headings = soup.select(".heading")
print(headings)