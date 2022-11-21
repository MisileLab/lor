from json import dumps, loads
from misilelibpy import read_once, write_once
from sys import stdin
from subprocess import run
from time import time

a = loads(read_once('data.json'))
b = 0
c = True
timedata = time()

while c:
    try:
        for i in stdin:
            if i.replace('\n', '') == "show":
                b += 1
                run("vim test.txt", shell=True)
            elif i == "":
                c = False
                break
    except KeyboardInterrupt:
        an = input("yes? y is yes")
        if an == "y":
            c = False
            break
    except Exception:
        pass
    

print(b)
a["data"].append(b)
a["timedata"].append(time() - timedata)
write_once('data.json', dumps(a))

