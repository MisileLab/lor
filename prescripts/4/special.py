from microbit import *
from library import *

a = False
b = 0

while True:
    if button_one_time_pressed(button_a) and button_one_time_pressed(button_b):
        a = False
        b = 0
        display.show(b)
    elif button_one_time_pressed(button_a):
        a = True
    elif button_one_time_pressed(button_b):
        a = False
        display.show(b)
    if a:
        b += max(accelerometer.get_x(), max(accelerometer.get_y(), accelerometer.get_z()))
