# Imports go at the top
from microbit import *
from library import *

a = 0
    
# Code in a 'while True:' loop repeats forever
while True:
    if button_one_time_pressed(button_a) or button_one_time_pressed(button_b):
        a += 1
    
    if a < 10:
        display.show(Image.HEART)
    elif a < 20:
        display.show(from_block_to_python("""
            . # . # .
                        # # # # #
                        # # . # #
                        . # # # .
                        . . # . .
        """))
    elif a < 30:
        display.show("""
            . # . # .
                        # . # . #
                        # # . # #
                        . # # # .
                        . . # . .
        """)
    elif a < 40:
        display.show("""
            . # . # .
                        # . . . #
                        # . . . #
                        . # # # .
                        . . # . .
        """)
    elif a < 50:
        display.show("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . # . .
        """)
    else:
        display.show("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)

