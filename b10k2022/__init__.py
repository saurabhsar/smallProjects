import matplotlib.pyplot as plt
import json
import urllib
from datetime import datetime

import pandas as pd

from commons.timewisefinishplot import plotFinishTime

timingData = json.load(open("datafile.json", "r"))

count = 0;

def convert(seconds):
    min, sec = divmod(seconds, 60)
    hour, min = divmod(min, 60)
    return datetime.strptime("%d:%02d:%02d" % (hour, min, sec), "%H:%M:%S")

def convertToMin(seconds):
    min, sec = divmod(seconds, 60)
    return min

def toSec(datetime):
    return datetime.hour * 3600 + datetime.minute * 60 + datetime.second

def toM(dist):
    return datetime.hour * 3600 + datetime.minute * 60 + datetime.second

plt.grid(True)

plt.xlabel('splitDistance')
plt.ylabel('speed km/h')

speed = []
splits = []
bibs = ["19409", "17411", "11018", "15112", "10020", "18329", "18071", "20095", "16007", "10019", "12555", "15088","19083"]

minWiseAtheleteCounter = {}

for athelete in timingData:

    chiptimeInMin = convertToMin(athelete['chiptime'])
    if chiptimeInMin not in minWiseAtheleteCounter:
        minWiseAtheleteCounter[chiptimeInMin] = 1;
    else:
        curr = minWiseAtheleteCounter[chiptimeInMin];
        minWiseAtheleteCounter[chiptimeInMin] = curr + 1;

    if athelete['bibNo'] not in bibs:
        continue;
    xAxis = []
    yAxis = []


    for lap in athelete['laps']:
        d = datetime.strptime(lap['splitDistance'], "%H:%M:%S")
        yAxis.append(float(lap['splitName'][:-3]) * 3600 / toSec(d))
        xAxis.append(lap['splitName'][:-3])

    xAxis.append(athelete['distance'])
    yAxis.append((athelete['distance'] * 3600 / athelete['chiptime'])*1)
    splits = xAxis

    speed.append(yAxis)

    plt.plot(xAxis, yAxis, label=athelete['name'])

    count = count + 1;
    if (count > 50):
        break;

plt.legend(bbox_to_anchor=(0.75, 1.15), ncol=4)
plt.show()

plotFinishTime(minWiseAtheleteCounter)