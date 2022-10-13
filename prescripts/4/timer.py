from microbit import *
from library import *
from time import sleep, sleep_ms

a = 0

while True:
    if button_one_time_pressed(button_a):
        if a == 9:
            a = 0
        else:
            a += 1
    display.show(a)
    if button_one_time_pressed(button_b):
        while a > 0:
            sleep(60)
            a -= 1
            display.show(a)
        for _ in range(10):
            display.show(Image.YES)
            sleep_ms(500)
            display.clear()
            sleep_ms(500)
