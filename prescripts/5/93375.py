a = []
e = []

for _ in range(int(input())):
    n, s, d = map(int, input().split(" "))
    b = {
        "n": n,
        "s": s,
        "d": d,
        "data": {}
    }

    for i in range(b['n']):
        c, d = map(int, input().split(" "))
        b['data'][d] = c

    a.append(b)

for i in a:
    d = 0
    m = 0
    while i["d"] - d > 0:
        g = []
        for i2 in i['data']:
            i['data'][i2] = i['data'][i2] - i['s']

        for i2, i3 in i['data'].items():
            if i3 <= 0:
                m += i2
                g.append(i2)

        for i2 in g:
            del i['data'][i2]

        d += 1
    e.append(m)

for i, i2 in enumerate(e):
    print(f"Data Set {i+1}:\n{i2}\n")
        
