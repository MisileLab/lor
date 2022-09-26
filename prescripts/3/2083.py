a = []

while True:
    b = input().split(" ")
    if b == ["#", "0", "0"]:
        break
    a.append({
        "name": b[0],
        "age": int(b[1]),
        "weight": int(b[2])
    })

for i in a:
    if i["age"] > 17 or i["weight"] >= 80:
        print(f"{i['name']} Senior")
    else:
        print(f"{i['name']} Junior")
