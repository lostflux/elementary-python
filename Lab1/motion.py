# imports
from cs1lib import *

global x
x = None
global y
y = None
global r
r = 20
key_w, key_s, key_a, key_d = None, None, None, None


# key_l, key_r, key_lr = False, False, False


def key_press(key):
    global key_w, key_s, key_a, key_d
    if key == "w":
        key_w = True
    if key == "s":
        key_s = True
    if key == "a":
        key_a = True
    if key == "d":
        key_d = True
    # print(key, key_l, key_r, key_lr)


def key_release(key):
    global key_w, key_s, key_a, key_d
    if key == "w":
        key_w = False
    if key == "s":
        key_s = False
    if key == "a":
        key_a = False
    if key == "d":
        key_d = False


def draw():
    set_clear_color(0, 0, 0, 1)
    clear()
    global x, y, r
    global key_w, key_s, key_a, key_d
    if x is None:  # Code to  initialize x and y to center of window on first run
        x, y = 200, 200
        set_stroke_width(2)
        set_stroke_color(1, 0, 0, 1)

    if not (key_w and key_s):
        if key_w:
            y -= 5
        if key_s:
            y += 5
    if not (key_a and key_d):
        if key_a:
            x -= 5
        if key_d:
            x += 5

    draw_circle(x, y, r)


start_graphics(draw, key_press=key_press, key_release=key_release)
