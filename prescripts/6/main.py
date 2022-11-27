from matplotlib import pyplot
from misilelibpy import read_once
from json import loads

a = loads(read_once("data.json"))

pyplot.plot(range(len(a["data"])), a["data"], a["timedata"])
try:
    pyplot.show()
except UserWarning:
    pyplot.savefig("mygraph.png")

