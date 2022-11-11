from tomli import loads
from json import loads as jload
from subprocess import Popen
from os import listdir, getcwd

def read_once(path: str):
    """Read a file once"""
    a = open(path, 'r')
    b = a.read()
    a.close()
    return b

langlist = [".py", ".rb"]
a = loads(read_once('test.toml'))
globalvals = a['global']
flist = []
for i in listdir(getcwd()):
    for i2 in langlist:
        if i.endswith(i2):
            flist.append(i.removesuffix(i2))
            break
d = []

for i, i2 in enumerate(flist):
    b = []
    config = a.get(i2, globalvals)
    for i3 in config["lang"]:
        s = ""
        if i3 == "python":
            s += "'python problems.py"
        elif i3 == "pypy":
            s += "'pypy problems.py"
        elif i3 == "rustpython":
            s += "'rustpython problems.py"
        elif i3 == "ruby":
            s += "'ruby --enable-yjit problems.rb"
        s += f" {i2}'"
        b.append(s)
    args = ['hyperfine --runs 1 --export-json test.json']
    args.extend(b)
    print(args)
    p = Popen(' '.join(args), shell=True)
    print(p.wait())
    for i3 in jload(read_once('test.json'))["results"]:
        if i3['times'][0] > config["time"]:
            print(f"{i3['command']} took {i3['times'][0]} seconds, which is more than {config['time']} seconds, so test failed")
            d.append(i3['command'])
        else:
            print(f"{i3['command']} took {i3['times'][0]} seconds, which is less than {config['time']} seconds, so test passed")

for i in d:
    print(f"Test failed {i}")
