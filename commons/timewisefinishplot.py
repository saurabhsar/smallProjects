import matplotlib.pyplot as plt
import numpy as np

timeArr = []
countArr = []


def prepare(timeToFinishCount):
    plt.grid(True)

    plt.xlabel('fiish time')
    plt.ylabel('Athelete count')

    for time in sorted(timeToFinishCount.keys()):
        timeArr.append(time)
        countArr.append(timeToFinishCount[time])


def plotFinishTime(timeToFinishCount):
    prepare(timeToFinishCount)
    plt.plot(timeArr, countArr)
    plt.xticks(np.arange(30, 150, step=5), rotation='vertical')
    plt.yticks(np.arange(1, 100, step=3))
    plt.show()
