from microbit import *

a = 0

def button_one_time_pressed(button: Button):
    return button.is_pressed() and button.was_pressed()

while True:
    display.show(a)
    if button_one_time_pressed(button_a) and button_one_time_pressed(button_b):
        a = 0
    elif button_one_time_pressed(button_a):
        a -= 1
    elif button_one_time_pressed(button_b):
        a += 1
    
