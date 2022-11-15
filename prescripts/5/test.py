from json import loads as jload
from os import getcwd, listdir
from subprocess import Popen
from modules.library import get_input_and_output

from tomli import loads


def read_once(path: str):
    """Read a file once"""
    e = open(path, 'r', encoding="utf8")
    f = e.read()
    e.close()
    return f

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
    args = [f"'{get_input_and_output(i2).input}'", "| hyperfine --runs 1 --export-json test.json --show-output"]
    config = a.get(i2, globalvals)
    for i3 in config["lang"]:
        if i3 == "python":
            s = f"'python {i2}.py'"
        elif i3 == "pypy":
            s = f"'pypy {i2}.py"
        elif i3 == "rustpython":
            s = f"'rustpython {i2}.py"
        elif i3 == "ruby":
            s = f"'ruby --enable-yjit {i2}.rb"
        else:
            raise ValueError("no support lang")
        args.append(s)
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
