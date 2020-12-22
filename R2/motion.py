# imports
from cs1lib import *

global x
x = None
global y
y = None
global r
r = 20
key_l, key_r, key_lr = None, None, None


# key_l, key_r, key_lr = False, False, False


def key_press(key):
    keys_down = key
    global key_l, key_r, key_lr
    global key_l, key_r, key_lr
    if key == "l":
        key_l = True
    if key == "r":
        key_r = True
    if key_l and key_r:
        key_lr = True
    print(key, key_l, key_r, key_lr)


# start_graphics(key_press)


def key_release(key):
    global key_l, key_r, key_lr
    if key == "l":
        key_l = False
    if key == "r":
        key_r = False
    if not key_l and key_r:
        key_lr = False


def draw():
    set_clear_color(0, 0, 0, 1)
    clear()
    global x, y, r
    global key_l, key_r, key_lr
    if x is None:  # Code to  initialize x and y to center of window on first run
        x, y = 200, 200
        set_stroke_width(2)
        set_stroke_color(1, 0, 0, 1)

    if key_lr:
        pass
    elif key_l:
        x, y = x + 5, y
    elif key_r:
        x, y = x - 5, y

    draw_circle(x, y, r)


start_graphics(draw, key_press=key_press, key_release=key_release)
# key_down("l")
