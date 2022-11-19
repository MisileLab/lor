from json import dumps, loads
from misilelibpy import read_once, write_once
from sys import stdin
from subprocess import run

a = loads(read_once('test.json'))
b = 0

for i in stdin:
    if i.replace('\n', '') == "show":
        b += 1
        run("vim test.txt")

print(b)
a["data"].append(b)
write_once('test.json', dumps(a))

