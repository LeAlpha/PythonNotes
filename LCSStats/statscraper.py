import sys
import requests
from bs4 import BeautifulSoup

url = "https://gol.gg/players/player-stats/802/season-S10/split-Spring/tournament-ALL/champion-ALL/"
webRequest = requests.get(url)
wsoup = BeautifulSoup(webRequest.text, 'html.parser')
tableBody = wsoup.find("div", {"class": "col-12 col-sm-6 rowbreak pb-3"})
statDescription = tableBody.find_all("td", {"class": "text-right"})
statValues = tableBody.find_all("td", {"class": "text-center"})

statdlist = []
statvlist = []

for i in statDescription:
    statdlist.append(i.text.strip())

for i in statValues:
    statvlist.append(i.text.strip())

statdict = dict(zip(statdlist, statvlist))
print(statdict)
