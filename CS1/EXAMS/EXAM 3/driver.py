# File Name: driver.py
# Author: AMITTAI JOEL SIAVAVA WEKESA
# Date: 22 October 2020
# Purpose: CS1 Exam 3: Bubble Driver


# Imports:
import random
from bubbleset import *
from cs1lib import *


# Defining constants:
WINDOW_WIDTH, WINDOW_HEIGHT = 400, 400


# Bubbles Driver
frames = 0
bset = Bubbleset(5)


# Function to pop random bubbles in the bubbleset:
def pop_random_bubbles(bubbleset, n):
    popped_bubbles = 0
    while popped_bubbles < n:
        index_to_pop = random.randint(0, len(bubbleset.blist) - 1)
        x = bubbleset.blist[index_to_pop].x
        y = bubbleset.blist[index_to_pop].y
        bubbleset.pop_bubbles(x, y)
        bubbleset.remove_popped_bubbles()
        popped_bubbles += 1


# main_draw function to be passed into start_graphics:
def main_draw():
    global bset, frames
    clear()
    bset.draw()
    bset.update()
    bset.remove_popped_bubbles()
    if frames != 0 and frames % 5 == 0:
        bset.add_bubbles(5)
    if frames != 0 and frames % 50 == 0:
        pop_random_bubbles(bset, len(bset.blist)/2)
    frames += 1


# Passing main_draw function into start_graphics:
start_graphics(main_draw, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, title="Bubbles")
