from simplefunctions import print_sqrt
from cs1lib import clear, draw_circle, start_graphics

def draw():
    clear()
    draw_circle(125, 100, 50)
    draw_circle(275, 100, 50)

start_graphics(draw)