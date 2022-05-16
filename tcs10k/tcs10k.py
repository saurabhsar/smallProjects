import numpy as np
import requests
import matplotlib.pyplot as plt
import pandas as pd
from bs4 import BeautifulSoup as bs
from datetime import datetime


def convert(seconds):
  min, sec = divmod(seconds, 60)
  hour, min = divmod(min, 60)
  return datetime.strptime("%d:%02d:%02d" % (hour, min, sec), "%H:%M:%S")

def toSec(datetime):
  print(datetime)
  return datetime.hour * 3600 + datetime.minute * 60 + datetime.second

def toM(dist):
  return datetime.hour * 3600 + datetime.minute * 60 + datetime.second

url = 'https://www.sportstimingsolutions.in/resultstable1.php?eventId=67028&bibno=%s&eventname=TCS+World+10K+Bengaluru+2022'

bibs = ["7828", "7059", "852","19325","1470","7605","1641","852","8388","26056","12758","7901"]
#bibs = ["7828"]
xpoints = [0,3,4.6,5.9,7,7.9,8.4,9,10]
for bib in bibs:
  ypoints = [0]
  speed = [0]
  response = requests.get(url.replace("%s",bib))
  soup = bs(response.content, 'html.parser')
  timing_table = soup.findAll("div", attrs={"table-responsive box-shadow-result"})
  #print(soup)
  table = soup.findAll('td',{'class': 'table-td'})
  print("#########################################"+bib)
  #print(table)
  #for index in [3,7,11,15,19,23,27,31]:
  yindex = 1
  for index in [1,5,9,13,17,21,25,29]:
    dt = table[index].text.replace("\t","").replace("\n","")
    d = datetime.strptime(dt, "%H:%M:%S")
    ypoints.append((toSec(d)))
    speed.append(float(18/5) * (float((xpoints[yindex] - xpoints[yindex - 1]) * 1000)) / float(ypoints[yindex]-ypoints[yindex - 1]))
    yindex=yindex+1
  print(ypoints)
  plt.plot(xpoints, speed, label=bib)

plt.legend(bbox_to_anchor =(0.75, 1.15), ncol = 4)

plt.show()

