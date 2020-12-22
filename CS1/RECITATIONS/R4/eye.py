from math import *
from cs1lib import *

class Eye:
    def __init__(self, x, y, rad, r = 0, g = 0, b = 1):
        # eye position and size
        self.x = x
        self.y = y
        self.rad = rad
        self.direction = 0

        # eye color
        self.r = r
        self.g = g
        self.b = b

    def lookat(self, lx, ly):
        self.direction = atan2(ly-self.y, lx-self.x)

    def draw(self):
        # draw outer circle
        enable_stroke()
        set_fill_color(1,1,1)
        draw_circle(self.x, self.y, self.rad)

        # draw inner circle
        set_fill_color(self.r, self.g, self.b)
        ix = 0.4 * self.rad * cos(self.direction) + self.x
        iy = 0.4 * self.rad * sin(self.direction) + self.y
        draw_circle(ix, iy, 0.5*self.rad)
