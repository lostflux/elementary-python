# Crowd class driver

from cs1lib import *
from face import Face

mx = 200
my = 200

def my_mmove(x, y):
    global mx, my
    mx = x
    my = y

def main():
    enable_smoothing()
    set_clear_color(1,1,1)

    clear()
    f.lookat( mx, my )
    f.draw()

f = Face(200, 200, 100)
start_graphics(main, mouse_move=my_mmove)
