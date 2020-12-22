# Crowd class driver

from cs1lib import *
from crowd import Crowd

mx = 200
my = 200

def my_mmove(x, y):
    global mx, my
    mx = x
    my = y

def main():
    set_clear_color(1,1,1)

    clear()
    crowd.lookat( mx, my )
    crowd.draw()

crowd = Crowd(20)
start_graphics(main, mouse_move=my_mmove)
