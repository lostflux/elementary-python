# Filename: solar.py
# Author : Amittai Joel Siavava Wekesa
# Date: October 19, 2020
# Purpose: Solar System Driver, Adapted from from earthmoon.py

from cs1lib import *
from system import System
from body import Body

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

TIME_SCALE = 5000         # real seconds per simulation second
PIXELS_PER_METER = 1 / 1e7  # distance scale for the simulation

FRAMERATE = 30              # frames per second
TIMESTEP = 1.0 / FRAMERATE  # time between drawing each frame


def main():

    set_clear_color(0, 0, 0)    # black background

    clear()

    # Draw the system in its current state.
    solar_system.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER)

    # Update the system for its next state.
    solar_system.update(TIMESTEP * TIME_SCALE)


# Defining sun and 4 planets:
sun = Body(1.98892e30, 0, 0, 0, 0, 15, 0.93, 0.62, 0.05)
mercury = Body(3.3e23, 7 * 5.79e7, 0, 0, 1.2 * 47.4e4, 2.87, 0, 1, 0)
earth = Body(5.97e24, 7 * 1.496e8, 0, 0, 1.2 * 29.8e4, 6.756, 0, 0, 1)
mars = Body(6.42e23, 7 * 2.279e8, 0, 0, 1.2 * 24.1e4, 5.11, 1, 0, 0)
jupiter = Body(1.898e27, 3 * 7.78e8, 0, 0, 1.9 * 13.1e4, 10.2, 1, 1, 0)

list_of_bodies = [sun, mercury, earth, mars, jupiter]

solar_system = System(list_of_bodies)

start_graphics(main, 2400, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, framerate=FRAMERATE)
