# File Name: stringart.py
# Author: AMITTAI JOEL SIAVAVA WEKESA
# Date: 11th October, 2020
# Purpose: SA 5 -- String Art


# Imports:
from cs1lib import *

# Defining constant to hold window title
TITLE = "String Art"


# Draw function:
def draw(a1, b1, a2, b2, c1, d1, c2, d2, number_of_strings):
    set_clear_color(0, 0, 0, 1)
    clear()
    set_stroke_width(3)
    set_stroke_color(1, 0, 0, 1)
    enable_stroke()
    draw_line(a1, b1, a2, b2)
    draw_line(c1, d1, c2, d2)

    # Picking the start coordinates of first line, end coordinates of second line
    x1, y1 = a1, b1
    x2, y2 = c2, d2

    # Finding the step interval of coordinates on each line
    x1_interval = (a2 - a1) / number_of_strings
    y1_interval = (b2 - b1) / number_of_strings
    x2_interval = (c1 - c2) / number_of_strings  # Flipped order because drawing in the reverse direction
    y2_interval = (d1 - d2) / number_of_strings  # Flipped order because drawing in the reverse direction

    set_stroke_width(1)
    r, g, b, alpha = 0, 0.5, 1, 1   # Initializing draw colors

    # While current x-coordinate along line 1 is less or equal to than the x-coordinate at endpoint of line 1
    while x1 <= a2:
        set_stroke_color(r, g, b, alpha)
        draw_line(x1, y1, x2, y2)
        r += 1 / number_of_strings
        g += 0.2 / number_of_strings
        b -= 1 / number_of_strings

        # Stepping by on the two lines the appropriate intervals
        x1 += x1_interval
        y1 += y1_interval
        x2 += x2_interval
        y2 += y2_interval


# Parameter-less function to run inside start_graphics and call draw() to run
def main():
    draw(25, 50, 50, 200, 350, 180, 200, 350, 25)


start_graphics(main, title=TITLE)
