# No converted
1.
def on_button_pressed_a():
    sprite.move(1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    sprite.move(-1)
input.on_button_pressed(Button.B, on_button_pressed_b)

sprite: game.LedSprite = None
sprite = game.create_sprite(2, 2)
2.
def on_button_pressed_a():
    global sprite
    sprite += -1
    basic.show_number(sprite)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    global sprite
    sprite = 0
    basic.show_number(sprite)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_b():
    global sprite
    sprite += 1
    basic.show_number(sprite)
input.on_button_pressed(Button.B, on_button_pressed_b)

sprite = 0
basic.show_number(0)
sprite = 0
3.
def on_forever():
    basic.show_leds("""
        # # # # #
                # # # # #
                # # # # #
                # # # # #
                # # # # #
    """)
    led.set_brightness(input.light_level())
basic.forever(on_forever)
4.
def on_forever():
    if 50 <= input.light_level():
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
    else:
        basic.show_leds("""
            # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
        """)
basic.forever(on_forever)
def on_button_pressed_a():
    global time
    time += 1
    if 5 < time:
        time = 0
    basic.show_number(time)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global time
    time = 0
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global time
    while 0 < time:
        basic.show_number(time)
        basic.pause(60000)
        time += -1
    for index in range(10):
        basic.show_icon(IconNames.YES)
        basic.pause(500)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
input.on_button_pressed(Button.B, on_button_pressed_b)

time = 0
time = 0
special:
def on_button_pressed_a():
    global 리스트
    리스트 = True
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_six_g():
    global time
    if 리스트:
        time += 6
input.on_gesture(Gesture.SIX_G, on_gesture_six_g)

def on_gesture_three_g():
    global time
    if 리스트:
        time += 3
input.on_gesture(Gesture.THREE_G, on_gesture_three_g)

def on_gesture_eight_g():
    global time
    if 리스트:
        time += 8
input.on_gesture(Gesture.EIGHT_G, on_gesture_eight_g)

def on_button_pressed_ab():
    global 리스트, time
    리스트 = False
    time = 0
    basic.show_number(0)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global 리스트
    리스트 = False
    basic.show_number(time)
input.on_button_pressed(Button.B, on_button_pressed_b)

time = 0
리스트 = False
리스트 = False
time = 0
