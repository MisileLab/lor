from secrets import SystemRandom

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = 0

for i in range(10000):
    a = SystemRandom().choices(x, k=2)
    if a[0] in [2, 4, 6, 8, 10] or a[1] in [2, 4, 6, 8, 10]:
        b += 1

print(f"result: {b}/10000")

