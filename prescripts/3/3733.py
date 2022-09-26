a = []

while True:
    try:
        a.append(input().split(' '))
    except EOFError:
        break

for i in a:
    b, c = int(i[0]), int(i[1])
    print(c // (b+1))
