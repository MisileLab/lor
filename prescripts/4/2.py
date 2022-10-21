from microbit import *
from library import *

l = 0

while True:
    if button_one_time_pressed(button_a):
        l += -1
        display.show(l)
    if accelerometer.was_gesture('shake'):
        l = 0
        display.show(l)
    if button_one_time_pressed(button_b):
        l += 1
        display.show(l)
