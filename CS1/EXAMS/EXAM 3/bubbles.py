# File Name: bubbles.py
# Author: AMITTAI JOEL SIAVAVA WEKESA
# Date: 22 October 2020
# Purpose: CS1 Exam 3: Bubbles Class

# Imports:
import random
from cs1lib import *

# Defining constants
WINDOW_WIDTH, WINDOW_HEIGHT = 400, 400


# Bubbles Class:
class Bubbles:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = random.randint(5, 15)
        self.popped = False

    def draw(self):
        if not self.popped:
            set_fill_color(1, 0, 0.5, 1)
            set_stroke_color(0, 0, 0, 1)
            draw_circle(self.x, self.y, self.size)

    def update(self):
        vx = random.randint(-5, 5)
        vy = random.randint(-2, -1)
        self.x += vx
        self.y += vy
        if self.x < 0 or self.x > WINDOW_WIDTH or self.y < 0 or self.y > WINDOW_HEIGHT:
            self.pop_bubble()

    def pop_bubble(self):
        self.popped = True
