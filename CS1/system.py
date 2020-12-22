# Filename: system.py
# Author : Amittai Joel Siavava Wekesa
# Date: October 19, 2020
# Purpose: System Class


# Imports
import math


G = 6.67384e-11


class System:
    def __init__(self, list_of_bodies):
        self.list_of_bodies = list_of_bodies

    def draw(self, half_width, half_height, scale):
        for body in self.list_bodies:
            body.draw(half_width, half_height, scale)

    def update(self, time_step):
        # x_operator = y_operator = 1
        for body in self.list_of_bodies:
            for other_body in self.list_of_bodies:
                if self.list_of_bodies.index(body) != self.list_of_bodies.index(other_body):
                    dx = body.x - other_body.x
                    dy = body.y - other_body.y
                    distance = math.sqrt((dx ** 2) + (dy ** 2))
                    acceleration = G * other_body.mass / distance ** 2
                    ax = acceleration * dx / distance
                    ay = acceleration * dy / distance
                    body.update(ax, ay, time_step)
