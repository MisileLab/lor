from microbit import *
from library import *

sprite = Sprite(2, 2)
while True:
    if button_one_time_pressed(button_a):
        sprite.add(1)
    elif button_one_time_pressed(button_b):
        sprite.substract(1)
