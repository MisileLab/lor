from microbit import *
from library import *
from random import randint

a = 0
b = 0
c = randint(0, 4)
d = randint(0, 4)

while True:
    sp = Sprite(0, 0)
    if button_one_time_pressed(button_a) and button_one_time_pressed(button_b):
        if a != c and b != d:
            display.show(Image.NO)
        else:
            display.show(Image.HEART)
        sleep(1000)
        display.show(all_light())
    elif button_one_time_pressed(button_a):
        sp.add(1, 0)
    elif button_one_time_pressed(button_b):
        sp.add(0, 1)
    display.show(sp.tostring())
    sleep(100)
    display.show(all_light())
    sleep(100)
