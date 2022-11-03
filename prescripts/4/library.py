from microbit import *

def button_one_time_pressed(button: Button):
    return button.is_pressed() and (button.was_pressed() != False)

def from_block_to_python(s: str, level: int = 9):
    a = 1
    b = 0
    st = ""
    for i in s:
        if a % 5 == 0 and b != 4:
            st = st + i + ":"
            a = 0
            b += 1
        else:
            st = st + i
        a += 1
    return Image(s.replace('.', '0').replace('#', str(level)))

class Sprite:
    def __init__(self, x: int, y: int):
        self.prevx = x
        self.prevy = y
        self.listlol = [
            ["0", "0", "0", "0", "0", ":"],
            ["0", "0", "0", "0", "0", ":"],
            ["0", "0", "0", "0", "0", ":"],
            ["0", "0", "0", "0", "0", ":"],
            ["0", "0", "0", "0", "0"]
        ]
        self.listlol[y+2][x] = "9"

    def add(self, x: int = 0, y: int = 0):
        x = self.prevx + x
        y = self.prevy + y
        self.listlol[self.prevy+2][self.prevx] = "0"
        self.listlol[y+2][x] = "9"
        self.prevx = x
        self.prevy = y

    def substract(self, x: int = 0, y: int = 0):
        x = self.prevx - x
        y = self.prevy - y
        self.listlol[self.prevy+2][self.prevx] = "0"
        self.listlol[y+2]

    def tostring(self):
        a = []
        for i in self.listlol:
            a.append("".join(i))
        return "".join(a)
