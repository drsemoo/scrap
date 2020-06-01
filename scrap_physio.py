from bs4 import BeautifulSoup
import requests

source = requests.get("https://www.wzayef.net/jobs")

soup = BeautifulSoup(source.content,"lxml")
job = soup.find_all("div",class_="job_box")
print(len(job))
for i in range(len(job)):
    fh = job[i].text
    print(fh)
    
    
    # for link in fh.find_all('a',href=True):
    #     url = link['href']
    #     source2 = requests.get(url)
    #     soup2 = BeautifulSoup(source2.content,"lxml")
    #     job2 = soup2.find_all("div",id="job_descr")
    #     print("----------------------------------------------------------------")
    #     print(job2)
    #     print("----------------------------------------------------------------")
