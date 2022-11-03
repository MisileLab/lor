from microbit import *
from library import *

while True:
    sp = Spritenop(0, 0)
    if button_one_time_pressed(button_a):
        sp.add(1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    if a != c and b != d:
        basic.show_icon(IconNames.NO)
    else:
        basic.show_icon(IconNames.HEART)
    basic.pause(1000)
    basic.clear_screen()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global b
    led.unplot(a, b)
    b += 1
    if b > 4:
        b = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

d = 0
c = 0
b = 0
a = 0
a = 0
b = 0
c = randint(0, 4)
d = randint(0, 4)

def on_forever():
    led.toggle(a, b)
    basic.pause(100)
basic.forever(on_forever)

# 2.
def on_button_pressed_a():
    a.change(LedSpriteProperty.X, -1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    a.change(LedSpriteProperty.X, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

c: game.LedSprite = None
a: game.LedSprite = None
a = game.create_sprite(2, 4)
b = 0

def on_forever():
    global c, b
    c = game.create_sprite(randint(0, 4), 0)
    for index in range(4):
        basic.pause(500)
        c.change(LedSpriteProperty.Y, 1)
    if c.is_touching(a):
        b += 1
        c.delete()
    else:
        game.set_score(b)
        game.game_over()
basic.forever(on_forever)
