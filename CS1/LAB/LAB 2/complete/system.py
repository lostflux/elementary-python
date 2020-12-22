# Filename: system.py
# Author : Amittai Joel Siavava Wekesa
# Date: October 19, 2020
# Purpose: System Class


# Imports:
import math

# Gravitational constant:
G = 6.67384e-11


# System Class:
class System:
    def __init__(self, list_of_bodies):
        self.list_of_bodies = list_of_bodies

    def draw(self, half_width, half_height, scale):
        for body in self.list_of_bodies:
            body.draw(half_width, half_height, scale)

    @staticmethod
    def compute_acceleration(body, other_body, ax, ay):
        dx = other_body.x - body.x
        dy = other_body.y - body.y
        distance = body.distance(other_body)
        # distance = math.sqrt((dx ** 2) + (dy ** 2))
        acceleration = G * other_body.mass / distance ** 2
        ax += acceleration * dx / distance
        ay += acceleration * dy / distance
        return ax, ay

    def update(self, time_step):
        for body in self.list_of_bodies:
            for other_body in self.list_of_bodies:
                ax, ay = 0, 0
                if body != other_body:
                    ax, ay = self.compute_acceleration(body, other_body, ax, ay)
                    body.update_velocity(ax, ay, time_step)
        for body in self.list_of_bodies:
            body.update_position(time_step)

