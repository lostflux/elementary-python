# FileName: lab 1 extracredit.py
# Author: AMITTAI JOEL SIAVAVA WEKESA
# Date: October 10, 2020
# Purpose: Lab 01 Assignment, Extra credit


# imports
from cs1lib import *
import random
import time
import math

# Initializing global variables and constants

left_bar_x, left_bar_y, right_bar_x, right_bar_y = None, None, None, None
key_a, key_z, key_k, key_m, key_space, key_q = None, None, None, None, None, None
PADDLE_WIDTH, PADDLE_HEIGHT, PADDLE_SPEED = 20, 80, 20
WINDOW_WIDTH, WINDOW_HEIGHT = 900, 600
LEFT_BAR_X, LEFT_BAR_INITIAL_Y, RIGHT_BAR_X, RIGHT_BAR_INITIAL_Y = 0, 0, WINDOW_WIDTH - 20, WINDOW_HEIGHT - 80
A, Z, K, M, SPACE, Q = "a", "z", "k", "m", " ", "q"  # Key values
left_paddle_color, right_paddle_color, ball_color = None, None, None
left_change, right_change = 0, 0
WINDOW_TITLE = "May the odds be ever in your favor!!"
START_TIME, NEW_TIME, end_time = time.time(), None, None
score, highest_score = 0, 0
GAME_BACKGROUND_COLOR = [0.3, 0.7, 0.4, 1]

# Ball stuff:
BALL_RADIUS = 20
BALL_INITIAL_VELOCITY_X, BALL_INITIAL_VELOCITY_Y = None, None
BALL_INITIAL_X, BALL_INITIAL_Y = WINDOW_WIDTH/2, WINDOW_HEIGHT/2
ball_position_x, ball_position_y = None, None
ball_velocity_x, ball_velocity_y = None, None
left_paddle_velocity, right_paddle_velocity = None, None
latest_game, total_played = 0, 0
ball_acceleration_y = None
ball_out_of_bounds, end_game_status = None, None

# Analytics:
full_analytics = None
latest_game_analytics = None
parting_shot = None


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


# Function to initialize the game on first run:
def initialize():
    global LEFT_BAR_X, LEFT_BAR_INITIAL_Y, RIGHT_BAR_X, RIGHT_BAR_INITIAL_Y
    global left_bar_y, right_bar_y, BALL_INITIAL_X, BALL_INITIAL_Y
    global ball_position_x, ball_position_y, ball_velocity_x, ball_velocity_y
    global ball_color, left_paddle_color, right_paddle_color
    global BALL_INITIAL_VELOCITY_X, BALL_INITIAL_VELOCITY_Y, NEW_TIME, score, highest_score
    global latest_game, total_played, ball_acceleration_y, ball_out_of_bounds, end_game_status
    ball_color, left_paddle_color, right_paddle_color = [1, 0, 0, 1], [0, 0, 1, 1], [0, 0, 1, 1]
    BALL_INITIAL_VELOCITY_X, BALL_INITIAL_VELOCITY_Y = random.randint(-10, 10) + 5, random.randint(-10, 10) + 5
    enable_stroke()
    left_bar_y, right_bar_y = LEFT_BAR_INITIAL_Y, RIGHT_BAR_INITIAL_Y
    set_stroke_width(2)
    ball_position_x, ball_position_y = BALL_INITIAL_X, BALL_INITIAL_Y
    if score > highest_score:
        highest_score = score
    score = 0
    NEW_TIME = time.time()

    # Ball Stuff:
    ball_position_x, ball_position_y = BALL_INITIAL_X, BALL_INITIAL_Y
    ball_acceleration_y = 0
    ball_out_of_bounds, end_game_status = False, False

    # To ensure ball always has meaningful x-component velocity:
    if BALL_INITIAL_VELOCITY_X in range(-3, 3):
        if BALL_INITIAL_VELOCITY_X < 0:
            ball_velocity_x = BALL_INITIAL_VELOCITY_X - 5
        elif BALL_INITIAL_VELOCITY_X > 0:
            ball_velocity_x = BALL_INITIAL_VELOCITY_X + 5
    else:
        ball_velocity_x = BALL_INITIAL_VELOCITY_X
    ball_velocity_y = BALL_INITIAL_VELOCITY_Y


# Function to control Paddle movement:
def paddle_movement():
    global key_a, key_z, key_k, key_m, key_space, key_q
    global left_bar_y, right_bar_y
    global PADDLE_SPEED, PADDLE_HEIGHT, WINDOW_HEIGHT
    global left_paddle_velocity, right_paddle_velocity
    # global left_change, right_change

    # Left paddle
    if not (key_a and key_z):

        # Left Paddle Up Movement:
        if key_a and left_bar_y - PADDLE_SPEED >= 0:
            left_bar_y -= PADDLE_SPEED  # Up Movement
            left_paddle_velocity = "up"
        elif key_a:
            left_bar_y = 0
            left_paddle_velocity = "none"
        # Left Paddle Down Movement:
        if key_z and left_bar_y + (PADDLE_HEIGHT + PADDLE_SPEED) <= WINDOW_HEIGHT:
            left_bar_y += PADDLE_SPEED  # Down Movement
            left_paddle_velocity = "down"
        elif key_z:
            left_bar_y = WINDOW_HEIGHT - PADDLE_HEIGHT
            left_paddle_velocity = "none"
        # Used upper-left corner for paddle coordinates

    # Right paddle:
    if not (key_k and key_m):

        # Right Paddle Up Movement:
        if key_k and right_bar_y - PADDLE_SPEED >= 0:
            right_bar_y -= PADDLE_SPEED  # Up Movement
            right_paddle_velocity = "up"
        elif key_k:
            right_bar_y = 0
            right_paddle_velocity = "none"

        # Right Paddle Down Movement:
        if key_m and right_bar_y + (PADDLE_HEIGHT + PADDLE_SPEED) <= WINDOW_HEIGHT:
            right_bar_y += PADDLE_SPEED  # Down Movement
            right_paddle_velocity = "down"
        elif key_m:
            right_bar_y = WINDOW_HEIGHT - PADDLE_HEIGHT
            right_paddle_velocity = "none"


# Function to control Ball movement:
def ball_movement():
    global ball_position_x, ball_position_y, ball_velocity_x, ball_velocity_y, WINDOW_WIDTH, WINDOW_HEIGHT
    global LEFT_BAR_X, left_bar_y, RIGHT_BAR_X, right_bar_y, PADDLE_WIDTH, BALL_RADIUS
    global right_paddle_color, left_paddle_color, ball_color, ball_out_of_bounds
    global left_change, right_change, score, ball_acceleration_y, left_paddle_velocity, right_paddle_velocity

    # Ball bouncing off paddles or ending game if Ball hits a vertical wall:
    if (ball_position_x - BALL_RADIUS) < PADDLE_WIDTH and ball_position_x > 0 - BALL_RADIUS:
        if round(ball_position_y) in range(math.floor(left_bar_y), math.ceil(left_bar_y + PADDLE_HEIGHT)):
            left_paddle_color = ball_color
            # Randomizing ball color:
            r = random.randint(500, 1000)
            g = random.randint(500, 1000)
            b = random.randint(500, 1000)
            ball_color = [abs(r + g - b) / 2000, abs(r - g + b) / 2000, abs(- r + g + b) / 2000, 1]
            ball_velocity_x = 0 - ball_velocity_x
            if left_paddle_velocity == "up":
                ball_acceleration_y = -3
            elif left_paddle_velocity == "down":
                ball_acceleration_y = 3
            if abs(ball_velocity_y + ball_acceleration_y) < 15:
                ball_velocity_y += ball_acceleration_y
            score += 5
    elif (ball_position_x + BALL_RADIUS) > RIGHT_BAR_X and ball_position_x < WINDOW_WIDTH + BALL_RADIUS:
        if round(ball_position_y) in range(math.floor(right_bar_y), math.ceil(right_bar_y + PADDLE_HEIGHT)):
            right_paddle_color = ball_color
            # Randomizing ball color:
            r = random.randint(500, 1000)
            g = random.randint(500, 1000)
            b = random.randint(500, 1000)
            ball_color = [abs(-r + g + b) / 2000, abs(r - g + b) / 2000, abs(r + g - b) / 2000, 1]
            ball_velocity_x = 0 - ball_velocity_x
            if right_paddle_velocity == "up":
                ball_acceleration_y = -3
            elif right_paddle_velocity == "down":
                ball_acceleration_y = 3
            if abs(ball_velocity_y + ball_acceleration_y) < 15:
                ball_velocity_y += ball_acceleration_y
            score += 5
    elif ball_position_x < 0 or ball_position_x > WINDOW_WIDTH:
        ball_out_of_bounds = True

    # Bouncing off top and bottom edges:
    if ball_position_y < 0 or ball_position_y > WINDOW_HEIGHT:
        ball_velocity_y = 0 - ball_velocity_y
        ball_acceleration_y = 0 - ball_acceleration_y

    ball_position_x += ball_velocity_x
    if abs(ball_velocity_y) < 10:
        ball_velocity_y += ball_acceleration_y
    elif ball_velocity_y > 0 > ball_acceleration_y:
        ball_velocity_y += ball_acceleration_y
    elif ball_velocity_y < 0 < ball_acceleration_y:
        ball_velocity_y += ball_acceleration_y
    # ball_velocity_y += ball_acceleration_y
    ball_position_y += ball_velocity_y

# Function to run when ending the game (i.e. when "Q" is pressed):
def finalize():
    global WINDOW_HEIGHT, end_time, key_space, score, highest_score, end_game_status
    global full_analytics, latest_game_analytics, parting_shot
    set_stroke_color(1, 0, 0, 1)
    set_fill_color(1, 0, 0, 1)
    end_game_status = True

    global end_time, latest_game, total_played
    if end_time is None:
        end_time = time.time()
        latest_game = end_time - NEW_TIME  # Time on current game
        total_played = end_time - START_TIME  # Total time played
    enable_stroke()
    set_stroke_color(1, 0, 0, 1)
    set_fill_color(1, 0, 0, 1)
    full_analytics = '''Congratulations, you have played a total of \n {0} minutes and {1} seconds'''.format(
        str(math.floor(total_played // 60)), str(round(total_played % 60)))
    latest_game_analytics = '''Your latest game was \n {0} minutes and {1} seconds.'''.format(
        str(math.floor(latest_game // 60)), str(round(latest_game % 60)))
    parting_shot = "Please  come back again!!"


def draw_to_canvas():
    global GAME_BACKGROUND_COLOR
    a, b, c, d = GAME_BACKGROUND_COLOR[0], GAME_BACKGROUND_COLOR[1], GAME_BACKGROUND_COLOR[2], GAME_BACKGROUND_COLOR[3]
    set_clear_color(0.3, 0.7, 0.4, 1)
    clear()
    set_stroke_color(left_paddle_color[0], left_paddle_color[1], left_paddle_color[2], left_paddle_color[3])
    set_fill_color(left_paddle_color[0], left_paddle_color[1], left_paddle_color[2], left_paddle_color[3])
    draw_rectangle(LEFT_BAR_X, left_bar_y, PADDLE_WIDTH, PADDLE_HEIGHT)

    set_stroke_color(right_paddle_color[0], right_paddle_color[1], right_paddle_color[2], right_paddle_color[3])
    set_fill_color(right_paddle_color[0], right_paddle_color[1], right_paddle_color[2], right_paddle_color[3])
    draw_rectangle(RIGHT_BAR_X, right_bar_y, PADDLE_WIDTH, PADDLE_HEIGHT)

    set_stroke_color(ball_color[0], ball_color[1], ball_color[2], ball_color[3])
    set_fill_color(ball_color[0], ball_color[1], ball_color[2], ball_color[3])
    draw_circle(ball_position_x, ball_position_y, BALL_RADIUS)
    set_stroke_color(1, 0, 0, 1)
    draw_text("Highest Score: " + str(highest_score), WINDOW_WIDTH - 150, 20)
    draw_text("Score: " + str(score), WINDOW_WIDTH - 150, 40)

    if end_game_status:
        draw_text(full_analytics, 20, WINDOW_HEIGHT / 2 - 200)
        draw_text(latest_game_analytics, 20, WINDOW_HEIGHT / 2 - 120)
        draw_text(parting_shot, 20, WINDOW_HEIGHT / 2 - 40)
        draw_text("HIGHEST SCORE: " + str(highest_score), WINDOW_WIDTH / 2 - 100, WINDOW_HEIGHT / 2 + 40)
        draw_text("LATEST SCORE: " + str(score), WINDOW_WIDTH / 2 - 100, WINDOW_HEIGHT / 2 + 120)
        draw_text("Press SPACE to close this window.", 20, WINDOW_HEIGHT / 2 + 200)
    elif ball_out_of_bounds:
        set_stroke_color(1, 0, 0, 1)
        draw_text("GAME OVER!! Press Space for a new game, or press Q to Quit",
                  WINDOW_WIDTH / 4, WINDOW_HEIGHT / 2)
        draw_text("Score: " + str(score), WINDOW_WIDTH / 2 - 20, WINDOW_HEIGHT / 2 + 40)


def run_all():
    global key_a, key_z, key_k, key_m, key_space, key_q
    global PADDLE_SPEED, PADDLE_WIDTH, PADDLE_HEIGHT, LEFT_BAR_X, left_bar_y, RIGHT_BAR_X, right_bar_y
    global WINDOW_TITLE, START_TIME, full_analytics, latest_game_analytics, parting_shot
    if key_space and key_q:  # Quiting window if Space is Pressed after Q is Pressed
        cs1_quit()
    elif key_space or left_bar_y is None:  # Initializing the game on first run
        initialize()
    elif key_q:  # Calling the finalize function when key Q is pressed
        finalize()
    else:  # Calling the functions to update ball and paddle positions
        paddle_movement()
        ball_movement()

    # Calling the function to draw to Canvas
    draw_to_canvas()


# Passing the draw function into start_graphics
start_graphics(run_all, title=WINDOW_TITLE, key_press=key_press, key_release=key_release, width=WINDOW_WIDTH,
               height=WINDOW_HEIGHT)
