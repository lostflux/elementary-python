# Filename: body.py
# Author : Amittai Joel Siavava Wekesa
# Date: October 19, 2020
# Purpose: Body Class


# Imports
from cs1lib import *
import math

class Body:
    def __init__(self, mass, x, y, vx, vy, pixel_radius, r, g, b):
        self.mass = mass
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.pixel_radius = pixel_radius
        self.color = [r, g, b]

    def distance(self, other_body):
        dx = self.x - other_body.x
        dy = self.y - other_body.y
        distance = math.sqrt((dx ** 2) + (dy ** 2))
        return distance

    def update(self, ax, ay, time_step):
        self.x -= self.vx * time_step
        self.y -= self.vy * time_step

        self.vx += ax * time_step
        self.vy += ay * time_step

    def draw(self, half_width, half_height, scale):
        red, green, blue = self.color[0], self.color[1], self.color[2]
        set_fill_color(red, green, blue)
        draw_circle(half_width + self.x * scale, half_height + self.y * scale, self.pixel_radius)
