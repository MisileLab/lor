a, b = 0, 0
c = False

for i in input():
  if i != "0" and c is False:
    a += int(i)
  elif i == "0" and c is False:
    a = a * 10
  elif i != "0" and c is True:
    b += int(i)
  else:
    b = b * 10

print(a+b)