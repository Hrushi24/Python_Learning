from bs4 import BeautifulSoup
import requests

#  for local sites
# with open("website.html", "r") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents , "html.parser")

responce = requests.get("https://news.ycombinator.com/show")

soup = BeautifulSoup(responce.text , "html.parser")

element = soup.select_one("table .titleline a")

print(element.text , element.get("href"))

headings = soup.select("table .titleline > a")
scores = soup.select("table .subtext .score")

articales= []
for i in range (0 , 20 , 1):

    articales.append((int(scores[i].text.split(" ")[0]) , headings[i].text , headings[i].get("href") ))
    # print(headings[i].text , "-> " , headings[i].get("href"))
    # print("Score -> ", int(scores[i].text.split(" ")[0]))



articales.sort(reverse=True)

for article in articales:
    print(article)
