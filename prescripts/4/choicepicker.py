from microbit import *
from library import *
from urandom import randint

b = 0
a = ["a", "b", "c", "d", "e"]

while True:
    if button_one_time_pressed(button_a):
        display.show(a[randint(0, len(a) - 1)])
