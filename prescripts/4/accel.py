# Imports go at the top
from microbit import *
from library import *

a = 0

# Code in a 'while True:' loop repeats forever
while True:
    if a == 0:
        display.show(from_block_to_python("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """))
    if button_one_time_pressed(button_a):
        display.show(a)
    b = accelerometer.current_gesture()
    if b == "6g":
        display.show(from_block_to_python("""
            . . . . .
                    . . . . .
                    # # # # #
                    # # # # #
                    # # # # #
        """))
        a += 3
    elif b == "freefall":
        display.show(from_block_to_python("""
            . . . . .
                    . . . . .
                    . . . . .
                    . . . . .
                    # # # # #
        """))
        a += 1
    elif b == "3g":
        display.show(from_block_to_python("""
            . . . . .
                    . . . . .
                    . . . . .
                    # # # # #
                    # # # # #
        """))
        a += 2
    elif b == "8g":
        display.show(from_block_to_python("""
            . . . . .
                    # # # # #
                    # # # # #
                    # # # # #
                    # # # # #
        """))
        a += 4
