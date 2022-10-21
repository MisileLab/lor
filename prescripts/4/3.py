from microbit import *
from library import *

while True:
    display.show(from_block_to_python("""
        # # # # #
                # # # # #
                # # # # #
                # # # # #
                # # # # #
    """, display.read_light_level()))
