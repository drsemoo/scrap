from bs4 import BeautifulSoup
import requests

ips = []
new_ip = []
with open ('ip_nc_27-5.txt',"r") as f :
    x = f.read()
    ips.append(x.split("\n"))


for ip in ips[0]:
    if ip == "":
        pass
    else:    
        source = requests.get("https://whatismyipaddress.com/ip/"+ip)

        soup = BeautifulSoup(source.content,"lxml")

        #dd = soup.find_all('div',id = "section_left_3rd")[0].table

        xx =soup.find_all("td")
        xy = soup.find_all("th")
        for i in range(len(xx)):
            print(f"{xy[i].text} : {xx[i].text}")



