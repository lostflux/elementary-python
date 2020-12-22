# Filename: system.py
# Author : Amittai Joel Siavava Wekesa
# Date: October 19, 2020
# Purpose: System Class


# Imports
import math


G = 6.67384e-11

class System:
    def __init__(self, list_of_bodies):
        self.bodies = list_of_bodies
        self.distances = {}
        for body in self.bodies:
            for other_body in self.bodies:
                initial_dx = body.x - other_body.x
                initial_dy = body.y - other_body.y
                distance = math.sqrt((initial_dx ** 2) + (initial_dy ** 2))
                self.distances[f"{self.bodies.index(body)} and {self.bodies.index(other_body)}"] = distance

    def draw(self, half_width, half_height, scale):
        for body in self.bodies:
            body.draw(half_width, half_height, scale)

    def update(self, time_step):
        x_operator = y_operator = 1
        earth = self.bodies[0]
        moon = self.bodies[1]
        dx = earth.x - moon.x
        dy = earth.y - moon.y
        distance = math.sqrt((dx ** 2) + (dy ** 2))
        for body in self.bodies:
            for other_body in self.bodies:
                if self.bodies.index(body) == self.bodies.index(other_body):
                    continue
                else:
                    dx = body.x - other_body.x
                    dy = body.y - other_body.y
                    acceleration = G * other_body.mass / distance ** 2
                    ax = acceleration * dx / distance
                    ay = acceleration * dy / distance
                    body.update(ax, ay, time_step)
