import matplotlib.pyplot as plt
import numpy as np

timeArr50 = []
countArr50 = []

timeArr60 = []
countArr60 = []

timeArr60p = []
countArr60p = []


def prepare(timeToFinishCount):
    plt.grid(True)

    plt.xlabel('fiish time')
    plt.ylabel('Athelete count')

    for time in sorted(timeToFinishCount.keys()):
        if time < 50:
            timeArr50.append(time)
            countArr50.append(timeToFinishCount[time])
        elif time < 60 :
            timeArr60.append(time)
            countArr60.append(timeToFinishCount[time])
        else:
            timeArr60p.append(time)
            countArr60p.append(timeToFinishCount[time])

def plotFinishTime(timeToFinishCount):
    prepare(timeToFinishCount)
    plt.plot(timeArr50, countArr50)
    plt.xticks(np.arange(30, 50, step=1), rotation='vertical')
    plt.yticks(np.arange(1, 100, step=2))
    plt.show()

    plt.plot(timeArr60, countArr60)
    plt.xticks(np.arange(50, 60, step=1), rotation='vertical')
    plt.yticks(np.arange(1, 100, step=2))
    plt.show()

    plt.plot(timeArr60p, countArr60p)
    plt.xticks(np.arange(60, 150, step=3), rotation='vertical')
    plt.yticks(np.arange(1, 100, step=3))
    plt.show()
