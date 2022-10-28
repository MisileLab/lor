a = []

for _ in range(int(input())):
    a.append(input().split(" "))

print("Gnomes:")
for i in a:
    i2 = i
    i2.sort()
    i3 = list(reversed(i2))
    if i == i2 or i == i3:
        print("Ordered")
    else:
        print("Unordered")