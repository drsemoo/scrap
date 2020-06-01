from bs4 import BeautifulSoup
import requests

source = requests.get("https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data")

soup = BeautifulSoup(source.content,"lxml")
stat = soup.find_all("tbody")[0]
summary = stat.find_all("tr")

summary1 = stat.find_all("tr")[2]
dd = summary1.find_all("th")
print(len(summary1))
# stat1 = stat.find_all("tr")[1].find_all("td")
#print(f"{1}-({dd[1].text}) : Confirmed cases :{dd[1].text} , Recovered cases :{dd[3].text} , Death :{dd[2].text}")


# for i in range(len(summary)):
#     summary1 = stat.find_all("tr")[i].th.a.text
#     stat1 = stat.find_all("tr")[i].find_all("td")
#     print(f"{i+1}-({summary1}) : Confirmed cases :{stat1[0].text} , Recovered cases :{stat1[2].text} , Death :{stat1[1].text}")


