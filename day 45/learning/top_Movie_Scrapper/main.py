from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

content = response.text

soup = BeautifulSoup(content , "html.parser")

allMovies = soup.select(".article-title-description__text > h3")



movieList = []
i = 1

for movie in allMovies:
    movieList.append([i ,movie.text])
    i += 1



    

movieList.sort(reverse=True)

# file creation and opening
with open("movies.txt" , "w" ,encoding="utf-8") as file:
    for mov in movieList:
        file.write(f"{mov[1]}\n")
        

# for mov in movieList:
#     print(f"{mov[1]}")

# print(allMovies)
