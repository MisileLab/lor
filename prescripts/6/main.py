from matplotlib import pyplot
from misilelibpy import read_once
from json import loads

a = loads(read_once("test.json"))

pyplot.plot(a["data"])
pyplot.show()

