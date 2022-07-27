#enter to venv to check the ouput and put the downloaded chromedriver  in vs
from bs4 import BeautifulSoup
import requests

try:
   response=requests.get("https://www.imdb.com/chart/top/")
   soup=BeautifulSoup(response.text,'html.parser')
   #print(soup)
   movies=soup.find('tbody',class_="lister-list").find_all("tr")

   for movie in movies:
  #  print(movie)
    rank=movie.find('td',class_="titleColumn").get_text(strip=True).split(',')[0]
    movie_name=movie.find('td',class_="titleColumn").a.text
    rate=movie.find('td',class_="ratingColumn").strong.text
    year=movie.find('td',class_="titleColumn").span.text.replace('(',"")
    year=year.replace(')',"")
    print(rank,movie_name,rate,year)

except Exception as e:
    print(e)
