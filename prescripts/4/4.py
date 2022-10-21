from library import *
from microbit import *

while True:
    if 50 <= input.light_level():
        display.show(from_block_to_python("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """))
    else:
        display.show(from_block_to_python("""
            # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
        """))
