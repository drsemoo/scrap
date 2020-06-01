from bs4 import BeautifulSoup
#import lxml
import requests

source = requests.get("https://news.google.com/covid19/map?hl=en-US&gl=US&ceid=US:en")

soup = BeautifulSoup(source.content,"lxml")

#dd = soup.find_all('table',class_="table-auto")[0]    #[0].h3.text
# dd1 = dd.find_all('tbody',class_="font-bold")[0]
# summary = dd1.find_all("tr")[0]
stat = soup.find_all("tbody")[0]
summary = stat.find_all("tr")
for i in range(len(summary)):
    summary1 = stat.find_all("tr")[i].th.text
    stat1 = stat.find_all("tr")[i].find_all("td")
    print(f"{i+1}-({summary1}) : Confirmed cases :{stat1[0].text} , Recovered cases :{stat1[2].text} , Death :{stat1[3].text}")

#print((summary1))


#print(f"USA {stat[0].text} is :{summary[0].text} \nUSA {stat[1].text} is :{summary[1].text} \nUSA {stat[2].text} is :{summary[2].text} \nUSA {stat1[0].text} is :{summary1[0].text} \n")