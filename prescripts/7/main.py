from matplotlib import pyplot
from json import loads
from misilelibpy import read_once

a = loads(read_once('data.json'))
daytime = []
for i, i2 in zip(a["dayhour"], a["daymin"]):
    daytime.append(i * 60 + i2)
sleepday = []
for i, i2 in zip(a["sleepdayhour"], a["sleepdaymin"]):
    sleepday.append(i * 60 + i2)
length = range(len(daytime))

pyplot.plot(length, daytime, sleepday)
pyplot.show()

