# File Name     : drawingboard.py
# Author        : AMITTAI JOEL SIAVAVA WEKESA
# Date          : September 2020
# Purpose       : SA4 -- Program to allow user to draw


# imports
from cs1lib import *

# Initialization of global non variables
x_old = None
y_old = None


def main():
    set_clear_color(0, 0, 0, 1)

    # Recalling global variables x_old, y_old
    global x_old
    global y_old
    if x_old is None:  # Code to run on first instance
        clear()  # Set board background to BLACK
        set_stroke_width(2)  # Set stroke width to 2
        set_stroke_color(1, 1, 1, 1)  # Initialize stroke color to WHITE

    # Switching Colors:
    #     "r" = RED
    #     "g" = GREEN
    #     "b" = BLUE
    #     "w" = WHITE
    #     "y" = YELLOW
    #     "o" = ORANGE
    #     "c" = CYAN
    #     "p" = PURPLE
    #     "a" = AQUA

    palettes = {"r": [1, 0, 0, 1], "g": [0, 1, 0, 1], "b": [0, 0, 1, 1],
                "w": [1, 1, 1, 1], "y": [1, 1, 0, 1], "o": [1, 1 / 2, 0, 1],
                "c": [0, 1, 1, 1], "p": [1 / 2, 0, 1 / 2, 1], "a": [0, 1, 1, 1]}
    keys = ["r", "g", "b", "w", "y", "o", "c", "p", "a"]
    for n in keys:
        if is_key_pressed(n):
            color = palettes[n]
            r, g, b, alpha = color[0], color[1], color[2], color[3]
            set_stroke_color(r, g, b, alpha)

    # Draw action when mouse is pressed and moved
    if is_mouse_pressed():
        if x_old is None or x_old == 0:
            x_old, y_old = mouse_x(), mouse_y()
        x, y = mouse_x(), mouse_y()
        draw_line(x, y, x_old, y_old)
        x_old, y_old = x, y

    # Reset x_old, y_old when the mouse press is released
    elif not is_mouse_pressed():
        x_old, y_old = 0, 0


start_graphics(main)
