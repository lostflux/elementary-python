# FileName: lab 1 checkpoint.py
# Author: Amittai Joel Wekesa
# Date: October 03, 2020
# Purpose: Lab 01 Assignment


# imports
from cs1lib import *

# Initializing global variables and constants
left_bar_x, left_bar_y, right_bar_x, right_bar_y = None, None, None, None
key_a, key_z, key_k, key_m, key_space, key_q = None, None, None, None, None, None
MOVEMENT = 5
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 80
WINDOW_WIDTH, WINDOW_HEIGHT = 400, 400
BALL_SIZE = 20
X_VELOCITY = 4
BALL_INITIAL_X, BALL_INITIAL_Y = 200, 200
LEFT_BAR_X, LEFT_BAR_INITIAL_Y, RIGHT_BAR_X, RIGHT_BAR_INITIAL_Y = 0, 0, 380, 320
left_bar_y, right_bar_y = None, None
A, Z, K, M, SPACE, Q = "a", "z", "k", "m", " ", "q"  # Key values


# Function for key_press events
def key_press(key):
    global key_a, key_z, key_k, key_m, key_space, key_q
    key = key.lower()
    if key == A:
        key_a = True
    if key == Z:
        key_z = True
    if key == K:
        key_k = True
    if key == M:
        key_m = True
    if key == SPACE:
        key_space = True
    if key == Q:
        key_q = True


# Function for key_release events
def key_release(key):
    global key_a, key_z, key_k, key_m, key_space, key_q
    key = key.lower()
    if key == A:
        key_a = False
    if key == Z:
        key_z = False
    if key == K:
        key_k = False
    if key == M:
        key_m = False
    if key == SPACE:
        key_space = False
    if key == Q:
        key_q = False


# Function to draw on Canvas
def draw():
    set_clear_color(1, 1, 0, 1)
    clear()
    # global x1, y1, x2, y2
    global key_a, key_z, key_k, key_m, key_space, key_q
    global MOVEMENT, PADDLE_WIDTH, PADDLE_HEIGHT, LEFT_BAR_X, left_bar_y, RIGHT_BAR_X, right_bar_y

    def initialize():  # Code to run when creating a new game
        global LEFT_BAR_X, LEFT_BAR_INITIAL_Y, RIGHT_BAR_X, RIGHT_BAR_INITIAL_Y
        global left_bar_y, right_bar_y
        enable_stroke()
        set_fill_color(1, 0, 0, 1)
        left_bar_y, right_bar_y = LEFT_BAR_INITIAL_Y, RIGHT_BAR_INITIAL_Y
        set_stroke_width(2)
        set_stroke_color(1, 0, 0, 1)
    if key_space or left_bar_y is None:
        initialize()

    # Updating the position of left bar depending on the pressed key
    if not (key_a and key_z):
        if key_a and left_bar_y - MOVEMENT >= 0:
            left_bar_y -= MOVEMENT  # Up Movement
        elif key_a:
            left_bar_y = 0

        if key_z and left_bar_y + (PADDLE_HEIGHT + MOVEMENT) <= WINDOW_HEIGHT:
            left_bar_y += MOVEMENT  # Down Movement
        elif key_z:
            left_bar_y = WINDOW_HEIGHT - PADDLE_HEIGHT
            # Used upper-left corner for paddle for coordinates

    # Updating the position of the right bar depending on the pressed key
    if not (key_k and key_m):
        if key_k and right_bar_y - MOVEMENT >= 0:
            right_bar_y -= MOVEMENT  # Up Movement
        elif key_k:
            right_bar_y = 0

        if key_m and right_bar_y + (PADDLE_HEIGHT + MOVEMENT) <= WINDOW_HEIGHT:
            right_bar_y += MOVEMENT  # Down Movement
        elif key_m:
            right_bar_y = WINDOW_HEIGHT - PADDLE_HEIGHT

    # Drawing to Canvas
    draw_rectangle(LEFT_BAR_X, left_bar_y, PADDLE_WIDTH, PADDLE_HEIGHT)
    draw_rectangle(RIGHT_BAR_X, right_bar_y, PADDLE_WIDTH, PADDLE_HEIGHT)
    # draw_circle(BALL_INITIAL_X, BALL_INITIAL_Y, BALL_SIZE)


# Passing the draw function into start_graphics
start_graphics(draw, key_press=key_press, key_release=key_release)
