# Filename  : drawing.py
# Author    : AMITTAI JOEL WEKESA
# Date      : September 2020
# Course    : COSC 1: Introduction to Programming
# Purpose   : SA3 -- Creating Animation of a Scene
# NOTE      : Color Palettes from https://flaviocopes.com/rgb-color-codes/


# imports
from cs1lib import *
import random


def main():  # Function to Draw a bedroom scene

    # Make Background Teal
    def make_background_teal():
        set_clear_color(70 / 255, 130 / 255, 180 / 255, 1)
        clear()

    # Draw the windows
    def draw_windows():
        set_fill_color(160 / 255, 82 / 255, 45 / 255, 1)
        draw_rectangle(20, 20, 190, 200)

        set_fill_color(25 / 255, 25 / 255, 112 / 255, 1)
        draw_rectangle(30, 30, 80, 180)

        set_fill_color(25 / 255, 25 / 255, 112 / 255, 1)
        draw_rectangle(120, 30, 80, 180)

    # Draw the stars
    def draw_moon_and_stars():

        # Draw the stars
        set_fill_color(1, 1, 1)
        for i in range(40):
            x = random.randint(30, 200)
            y = random.randint(30, 200)
            r = random.randint(20, 200) / 50
            if (y - r) > 30 and (y + r) < 200:
                if (x - r) > 30 and (x + r) < 100:
                    draw_circle(x, y, r)
                elif (x - r) > 120 and (x + r) < 200:
                    draw_circle(x, y, r)

        # Draw the moon
        set_fill_color(1, 1, 0)
        draw_circle(50, 60, 20)

    # Draw Bookshelf
    def draw_bookshelf():
        set_fill_color(205 / 255, 92 / 255, 92 / 255)
        draw_rectangle(250, 80, 120, 20)

    # Draw books
    def draw_books():
        set_fill_color(0, 128 / 255, 128 / 255)
        x, y = 250, 30
        while x < 370:
            draw_rectangle(x + 5, y, 10, 50)
            x += 20

    # Draw the bed
    def draw_bed():
        x, y = 30, 320
        set_fill_color(205 / 255, 92 / 255, 92 / 255)
        draw_rectangle(x, y, 15, 80)
        draw_rectangle(x + 250, y + 20, 15, 60)
        draw_rectangle(x + 15, y + 30, 235, 20)
        set_fill_color(72 / 255, 61/255, 139/255)
        draw_rectangle(x + 15, y + 30, 235, -10)

    # Draw the poster on the wall
    def draw_poster():
        set_fill_color(160 / 255, 82 / 255, 45 / 255, 1)
        draw_rectangle(250, 120, 120, 120)

        set_fill_color(184 / 255, 134 / 255, 11 / 255, 1)
        draw_rectangle(260, 130, 100, 100)

    # Print words in poster
    def print_to_poster():
        # Printing names
        set_fill_color(0, 0, 0, 1)
        txt = "AMITTAI JOEL WEKESA"
        draw_text(txt.split(" ")[0], 280, 150)
        draw_text(txt.split(" ")[1], 280, 180)
        draw_text(txt.split(" ")[2], 280, 210)

        # Drawing lines under name
        x, y = 270, 155
        for i in range(3):
            draw_line(x, y, x + 80, y)
            y += 30

    # Function to call all the other functions
    def run():
        make_background_teal()
        draw_windows()
        draw_moon_and_stars()
        draw_bookshelf()
        draw_books()
        draw_bed()
        draw_poster()
        print_to_poster()

    # Making the function call
    run()


# Passing the "main" function into start_graphics
start_graphics(main)
