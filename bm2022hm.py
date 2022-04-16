import matplotlib.pyplot as plt
import json
import urllib
from datetime import datetime
import plotly.express as px
import pandas as pd

timingData = json.loads(urllib.request.urlopen("https://api.racetime.tk/v1/result/bd5549bd-0873-42a4-ae05-dfadafc5601b/All%20Categories/21.1%20Km/overall").read().decode())

plt.grid(True)

plt.xlabel('splitDistance')
plt.ylabel('speed')

count = 0;

def convert(seconds):
    min, sec = divmod(seconds, 60)
    hour, min = divmod(min, 60)
    return datetime.strptime("%d:%02d:%02d" % (hour, min, sec), "%H:%M:%S")

def toSec(datetime):
    return datetime.hour * 3600 + datetime.minute * 60 + datetime.second

def toM(dist):
    return datetime.hour * 3600 + datetime.minute * 60 + datetime.second

speed = []
splits = []
bibs = ["25751", "21643","24131","21124","25803","24055","24890","25782","24035","21275","21553","25819","21648"]

for athelete in timingData:
    if athelete['bibNo'] not in bibs:
        continue;
    xAxis = []
    yAxis = []
    
    for lap in athelete['laps']:
        d = datetime.strptime(lap['splitDistance'], "%H:%M:%S")
        yAxis.append(float(lap['splitName'][:-3])* 1000 / toSec(d))
        xAxis.append(lap['splitName'][:-3])
        
    xAxis.append(athelete['distance'])
    yAxis.append(athelete['distance'] * 1000 / athelete['chiptime'])
    splits = xAxis
    
    speed.append(yAxis)
    
    plt.plot(xAxis, yAxis, label=athelete['name'])
    
    count = count + 1;
    if (count > 50) :
        break;
        
plt.legend(bbox_to_anchor =(0.75, 1.15), ncol = 4)
plt.show()
fig.show()
