# Filename: solar.py
# Author : Amittai Joel Siavava Wekesa
# Date: October 19, 2020
# Purpose: Simulation of full solar system

# Imports
from cs1lib import *
from system import System
from body import Body
import math
import random
import time


# Initializing constants:
WINDOW_WIDTH = 1440
WINDOW_HEIGHT = 1440
G = 6.67384e-11

TIME_SCALE = 5000         # real seconds per simulation second
PIXELS_PER_METER = 1 / 1e7  # distance scale for the simulation

FRAMERATE = 30              # frames per second
TIMESTEP = 1.0 / FRAMERATE  # time between drawing each frame
WINDOW_TITLE = "Solar System"
# Initializing variables to be used in adding planets:
x, y, press_detector = 0, 0, False
start_time = 0


# Function to handle mouse-press events
def mouse_pressed(mx, my):
    global press_detector, start_time
    start_time = time.time()
    press_detector = True


# Function to run when mouse is released
def mouse_released(mx, my):
    global earth, sun, solar_system, x, y, press_detector
    if press_detector:
        end_time = time.time()
        x, y = mx - 720, my - 720
        x /= PIXELS_PER_METER
        y /= PIXELS_PER_METER
        dx = sun.x - x
        dy = sun.y - y
        new_radius = (end_time - start_time) * earth.pixel_radius
        body_distance = math.sqrt((dx ** 2) + dy ** 2)
        earth.speed = math.sqrt((earth.vx ** 2) + (earth.vy ** 2))
        mass = earth.mass * new_radius / earth.pixel_radius
        v = math.sqrt(G * sun.mass / body_distance)
        vx = v * dy / body_distance
        vy = v * dx / body_distance
        red = random.randint(10, 100) / 100
        green = random.randint(10, 100) / 100
        blue = random.randint(10, 100) / 100
        new_body = Body(mass, x, y, vx, vy, new_radius, red, green, blue)
        solar_system.list_of_bodies.append(new_body)
        press_detector = False


# Main function to be passed into start_graphics:
def main():

    set_clear_color(0, 0, 0)    # black background

    clear()

    # Draw the system in its current state.
    set_stroke_color(1, 0, 0.5, 1)
    set_stroke_width(5)
    draw_text("Press and hold the mouse pointer to add planets.", 720, 50)
    set_stroke_width(1)
    set_stroke_color(0, 0, 0, 0)
    solar_system.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER)

    # Update the system for its next state.
    solar_system.update(TIMESTEP * TIME_SCALE)


# Creating the bodies:
sun = Body(1.98892e30, 0, 0, 0, 0, 15, 0.93, 0.62, 0.05)
mercury = Body(3.3e23, 7 * 5.79e7, 0, 0, 1.2 * 47.4e4, 2.87, 0, 1, 0)
venus = Body(4.87e24, 7 * 1.082e8, 0, 0, 1.2 * 35.0e4, 3.104, 1, 1, 1)
earth = Body(5.97e24, 7 * 1.496e8, 0, 0, 1.2 * 29.8e4, 6.756, 0, 0, 1)
mars = Body(6.42e23, 7 * 2.279e8, 0, 0, 1.2 * 24.1e4, 5.11, 1, 0, 0)
jupiter = Body(1.898e27, 3 * 7.78e8, 0, 0, 1.9 * 13.1e4, 10.2, 1, 1, 0)
saturn = Body(5.68e26, 2 * 1.433e9, 0, 0, 2.5 * 9.7e4, 9.76, 0.8, 0.6, 0.05)
uranus = Body(8.68e25, 1.3 * 2.872e9, 0, 0, 3.2 * 6.7e4, 7.77, 0, 0.8, 0.8)
neptune = Body(1.02e26, 4.495e9, 0, 0, 3.6 * 5.4e4, 4.9528, 0.4, 0, 0.4)
pluto = Body(1.4e22, 0.9 * 5.906e9, 0, 0, 3.7 * 4.7e4, 2.37, 0.8, 0.8, 0)

list_of_bodies = [sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune, pluto]

solar_system = System(list_of_bodies)

# Passing the main function into start_graphics
start_graphics(main, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, framerate=FRAMERATE,
               mouse_press=mouse_pressed, mouse_release=mouse_released, title=WINDOW_TITLE)
