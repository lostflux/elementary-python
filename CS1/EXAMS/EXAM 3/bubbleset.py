# File Name: bubbleset.py
# Author: AMITTAI JOEL SIAVAVA WEKESA
# Date: 22 October 2020
# Purpose: CS1 Exam 3: Bubbleset Class

# Imports:
from bubbles import *

# Defining constants:
WINDOW_WIDTH, WINDOW_HEIGHT = 400, 400


# Bubbleset Class:
class Bubbleset:
    def __init__(self, n):
        self.blist = []
        self.add_bubbles(n)

    def update(self):
        for bubble in self.blist:
            bubble.update()

    def draw(self):
        for bubble in self.blist:
            bubble.draw()

    def add_bubbles(self, n):
        for i in range(n):
            self.blist.append(Bubbles(WINDOW_WIDTH / 2, WINDOW_HEIGHT))

    def pop_bubbles(self, x, y):
        for bubble in self.blist:
            if bubble.x == x and bubble.y == y:
                bubble.pop_bubble()

    def remove_popped_bubbles(self):
        for bubble in self.blist:
            if bubble.popped:
                self.blist.remove(bubble)
