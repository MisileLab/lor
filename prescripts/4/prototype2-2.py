# I don't know how do I display it

from microbit import *
from library import *
from random import randint
from log import add

a = Sprite(2, 4)
b = 0
c = Sprite(randint(0, 4), 0)

while True:
    if button_one_time_pressed(button_a):
        a.add(-1)
    for _ in range(4):
        sleep(500)
        c.add(0, 1)
    if c.prevx == a.prevx:
        b += 1
        c = Sprite(randint(0, 4), 0)
    else:
        add({"score": b})
        break
