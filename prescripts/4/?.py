from microbit import *
from library import *

time = 0

while True:
    if button_one_time_pressed(button_a) and button_one_time_pressed(button_b):
        time = 0
        display.show(time)
    elif button_one_time_pressed(button_a):
        time += 1
        if time > 5:
            time = 0
        display.show(time)
    elif button_one_time_pressed(button_b):
        while time > 0:
            display.show(time)
            sleep(60000)
            time -= 1
        for i in range(10):
            display.show(Image.YES)
            sleep(500)
            display.show(from_block_to_python(
                """
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """
            ))
