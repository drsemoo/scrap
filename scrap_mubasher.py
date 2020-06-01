



from bs4 import BeautifulSoup
import requests

source = requests.get("https://www.mubasher.info/countries/eg/stock-prices")

soup = BeautifulSoup(source.content,"lxml")

#dd = soup.find_all('tr')[1]
summary = soup.find_all("td",class_="mi-hide-for-small")[2].rows

print(summary)



