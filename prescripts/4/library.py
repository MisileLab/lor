from microbit import *

def button_one_time_pressed(button: Button):
    return button.is_pressed() and (button.was_pressed() != False)

def from_block_to_python(s: str, level: int = 9):
    return Image(s.replace('.', '0').replace('#', str(level)))
