# FileName: old lab 1 complete.py
# Author: Amittai Joel Wekesa
# Date: October 03, 2020
# Purpose: Lab 01 Assignment


# imports
from cs1lib import *

# Initializing global variables and constants
left_bar_x, left_bar_y, right_bar_x, right_bar_y = None, None, None, None
key_a, key_z, key_k, key_m, key_space, key_q = None, None, None, None, None, None
PADDLE_WIDTH, PADDLE_HEIGHT, PADDLE_SPEED = 20, 80, 20
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
LEFT_BAR_X, LEFT_BAR_INITIAL_Y, RIGHT_BAR_X, RIGHT_BAR_INITIAL_Y = 0, 0, WINDOW_WIDTH - 20, WINDOW_HEIGHT - 80
ball_color, left_paddle_color, right_paddle_color = None, None, None 
A, Z, K, M, SPACE, Q = "a", "z", "k", "m", " ", "q"  # Key values

# Ball stuff:
BALL_RADIUS = 20
BALL_INITIAL_VELOCITY_X, BALL_INITIAL_VELOCITY_Y = 5, 5
BALL_INITIAL_X, BALL_INITIAL_Y = 200, 100
ball_position_x, ball_position_y = None, None
ball_velocity_x, ball_velocity_y = None, None


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
    # if key == Q:
    #     key_q = False


# Function to draw on Canvas
def draw():
    set_clear_color(0.3, 0.7, 0.4, 1)
    clear()
    # global x1, y1, x2, y2
    global key_a, key_z, key_k, key_m, key_space, key_q
    global PADDLE_SPEED, PADDLE_WIDTH, PADDLE_HEIGHT, LEFT_BAR_X, left_bar_y, RIGHT_BAR_X, right_bar_y

    def initialize():  # Code to run when creating a new game
        global LEFT_BAR_X, LEFT_BAR_INITIAL_Y, RIGHT_BAR_X, RIGHT_BAR_INITIAL_Y
        global left_bar_y, right_bar_y, BALL_INITIAL_X, BALL_INITIAL_Y
        global ball_position_x, ball_position_y, ball_velocity_x, ball_velocity_y
        enable_stroke()
        set_fill_color(1, 0, 0, 1)
        left_bar_y, right_bar_y = LEFT_BAR_INITIAL_Y, RIGHT_BAR_INITIAL_Y
        set_stroke_width(2)
        set_stroke_color(1, 0, 0, 1)
        ball_position_x, ball_position_y = BALL_INITIAL_X, BALL_INITIAL_Y

        # Ball Stuff:
        ball_position_x, ball_position_y = BALL_INITIAL_X, BALL_INITIAL_Y
        ball_velocity_x, ball_velocity_y = BALL_INITIAL_VELOCITY_X, BALL_INITIAL_VELOCITY_Y

    def ball_movement():
        global ball_position_x, ball_position_y, ball_velocity_x, ball_velocity_y, WINDOW_WIDTH, WINDOW_HEIGHT
        global LEFT_BAR_X, left_bar_y, RIGHT_BAR_X, right_bar_y, PADDLE_WIDTH, BALL_RADIUS
        
        # Bouncing off paddles or ending game:
        if (ball_position_x - BALL_RADIUS) < PADDLE_WIDTH and ball_position_x > 0 - BALL_RADIUS:
            if ball_position_y in range(left_bar_y, left_bar_y + PADDLE_HEIGHT):
                ball_velocity_x = 0 - ball_velocity_x
        elif (ball_position_x + BALL_RADIUS) > RIGHT_BAR_X and ball_position_x < WINDOW_WIDTH + BALL_RADIUS:
            if ball_position_y in range(right_bar_y, right_bar_y + PADDLE_HEIGHT):
                ball_velocity_x = 0 - ball_velocity_x
        elif ball_position_x < 0 or ball_position_x > WINDOW_WIDTH:
            draw_text("GAME OVER!!", WINDOW_WIDTH/2 - 20, WINDOW_HEIGHT/2)

        # Bouncing off top and bottom edges:
        if ball_position_y < 0 or ball_position_y > WINDOW_HEIGHT:
            ball_velocity_y = 0 - ball_velocity_y

        ball_position_x += ball_velocity_x
        ball_position_y += ball_velocity_y

    def paddle_movement():
        global key_a, key_z, key_k, key_m, key_space, key_q
        global left_bar_y, right_bar_y
        global PADDLE_SPEED, PADDLE_HEIGHT, WINDOW_HEIGHT

        # Left bar
        if not (key_a and key_z):

            # Up Movement:
            if key_a and left_bar_y - PADDLE_SPEED >= 0:
                left_bar_y -= PADDLE_SPEED  # Up Movement
            elif key_a:
                left_bar_y = 0
            # Down Movement:
            if key_z and left_bar_y + (PADDLE_HEIGHT + PADDLE_SPEED) <= WINDOW_HEIGHT:
                left_bar_y += PADDLE_SPEED  # Down Movement
            elif key_z:
                left_bar_y = WINDOW_HEIGHT - PADDLE_HEIGHT
            # Used upper-left corner for paddle for coordinates

        # Right bar:
        if not (key_k and key_m):

            # Up Movement:
            if key_k and right_bar_y - PADDLE_SPEED >= 0:
                right_bar_y -= PADDLE_SPEED  # Up Movement
            elif key_k:
                right_bar_y = 0

            # Down Movement:
            if key_m and right_bar_y + (PADDLE_HEIGHT + PADDLE_SPEED) <= WINDOW_HEIGHT:
                right_bar_y += PADDLE_SPEED  # Down Movement
            elif key_m:
                right_bar_y = WINDOW_HEIGHT - PADDLE_HEIGHT

    # Drawing to Canvas
    def draw_to_canvas():
        global LEFT_BAR_X, RIGHT_BAR_X, left_bar_y, right_bar_y, PADDLE_WIDTH, PADDLE_HEIGHT
        global ball_position_x, ball_position_y, BALL_RADIUS
        draw_rectangle(LEFT_BAR_X, left_bar_y, PADDLE_WIDTH, PADDLE_HEIGHT)
        draw_rectangle(RIGHT_BAR_X, right_bar_y, PADDLE_WIDTH, PADDLE_HEIGHT)
        draw_circle(ball_position_x, ball_position_y, BALL_RADIUS)

    # Calling All Functions:
    if key_space or left_bar_y is None:
        initialize()
    elif key_q:
        cs1_quit()
    else:
        paddle_movement()
        ball_movement()
    draw_to_canvas()


# Passing the draw function into start_graphics
start_graphics(draw, key_press=key_press, key_release=key_release, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)