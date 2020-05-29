from bs4 import BeautifulSoup
import requests

source = requests.get("https://coronavirus-live-tracker.com/")

soup = BeautifulSoup(source.content,"lxml")

dd = soup.find_all('tbody')[0]  
summary = dd.find_all("tr")
for i in range(len(summary)):
    summar = dd.find_all("tr")[i]
    stat = summar.find_all("td")
    print(f"{stat[0].text}-{stat[1].span.text} confirmed:{stat[2].text} active:{stat[3].text} Death:{stat[4].text} Recovered:{stat[5].text} Critical:{stat[6].text} Today-cases:{stat[7].text} Today-death:{stat[8].text}")



