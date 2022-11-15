from sys import argv

probnum = argv[1]

class Timer:
    def __init__(self, hs: map):
        h, m, s = hs
        self.h = h
        self.m = m
        self.s = s

    def add_second(self, s: int):
        if s >= 60:
            m = (s - s % 60) / 60
            s = s % 60
            a = self.add_minute(m)
            if a is not None and a <= 24:
                self.s = 0
            self.add_second(s)
        elif s + self.s >= 60:
            self.add_minute(1)
            self.s = (s + self.s) - 60
        else:
            self.s += s
    
    def add_minute(self, m: int):
        if m >= 60:
            h = (m - m % 60) / 60
            if h >= 24:
                self.m = 0
            m = m % 60
            self.add_hour(h)
            self.add_minute(m)
            return h
        elif m + self.m >= 60:
            self.add_hour(1)
            self.m = (m + self.m) - 60
        else:
            self.m += m
        return None

    def add_hour(self, h: int):
        if self.h + h >= 24:
            h = (self.h + h) % 24
            self.h = 0
        self.h += h

    def add_time(self, s: int):
        if s >= 3600:
            self.add_hour((s - s % 3600) / 3600)
            s = s % 3600
        if s >= 60:
            self.add_minute((s - s % 60) / 60)
            s = s % 60
        self.add_second(s)
        self.h = int(self.h)
        self.m = int(self.m)
        self.s = int(self.s)
        return " ".join([str(self.h), str(self.m), str(self.s)])

def p1003():
    
    n = []
    n2 = []

    for _ in range(int(input())):
        n.append(int(input()))

    c = {}

    def fibo(d: int):
        if d == 0:
            return {"a": 1, "b": 0}
        elif d == 1:
            return {"a": 0, "b": 1}
        else:
            if c.get(d) is None:
                e = [fibo(d-1), fibo(d-2)]
                c[d] = {"a": e[0]["a"] + e[1]["a"], "b": e[0]["b"] + e[1]["b"]}
        return c[d]

    for i in n:
        print(f"{fibo(i)['a']} {fibo(i)['b']}")

def p2530():
    print(Timer(map(int, input().split(" "))).add_time(int(input())))

def p2742():
    for i in range(int(input())).__reversed__():
        print(i+1)


