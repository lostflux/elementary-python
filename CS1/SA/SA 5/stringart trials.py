# File Name: stringart.py
# Author: AMITTAI JOEL SIAVAVA WEKESA
# Date: 11th October, 2020
# Purpose: SA 5 -- String Art

# Imports:
import random

from cs1lib import *
import time


RED = random.randint(0, 5000) / 10000
GREEN, BLUE = RED - 0.3, RED + 0.4
A = 0.01
# red_step, green_step, blue_step, alpha_step = 0.01, 0.02, 0.03, 0.001
red_step = random.randint(50, 150) / 1000
green_step = random.randint(50, 150) / 1000
blue_step = random.randint(50, 105) / 1000
alpha_step = random.randint(50, 150) / 10000

fine, alpha_fine, red_fine, green_fine, blue_fine = None, None, None, None, None
re, gr, bl, alpha = None, None, None, None
a_factor, b_factor, c_factor, d_factor, e_factor, f_factor, g_factor, h_factor = 4, -4, -4, 4, -4, -4, -4, 4
strings = 500
dimension = []
for k in range(1, 799):
    dimension.append(k)
dimension1, dimension2 = [], []
WINDOW_WIDTH = [800, 800]
for i in range(1, 399):
    dimension1.append(i)
for j in range(401, 799):
    dimension2.append(j)
a2_factor, b2_factor, c2_factor, d2_factor = -0.1, -0.1, -0.1, -0.1
e2_factor, f2_factor, g2_factor, h2_factor = -0.1, -0.1, -0.1, -0.1

# Draw function:
def draw(a1, b1, a2, b2, c1, d1, c2, d2, number_of_strings):
    global fine, red_fine, green_fine, blue_fine, re, gr, bl, alpha, alpha_fine, fine
    x1_intervals = []
    y1_intervals = []
    x2_intervals = []
    y2_intervals = []

    # Conditional statements to ensure string interval is evaluated in the same order
    # irrespective of which edges are provided first
    # if a1 > a2:
    #     a1, b1, a2, b2 = a2, b2, a1, b1
    #     print("flipped 1")
    # if c1 < c2:
    #     c1, d1, c2, d2 = c2, d2, c1, d1
    #     print("flipper 2")
    x1_steps = (a2 - a1) * fine
    x2_steps = (c2 - c1) * fine
    y1_steps = (b2 - b1) * fine
    y2_steps = (d2 - d1) * fine
    for string in range(number_of_strings + 1):
        x1_intervals.append(a1 + string * x1_steps)
        y1_intervals.append(b1 + string * y1_steps)
        x2_intervals.append(c2 - string * x2_steps)
        y2_intervals.append(d2 - string * y2_steps)

    set_clear_color(0, 0, 0, 1)
    clear()
    set_stroke_width(3)
    set_stroke_color(1, 0, 0, 1)
    draw_line(a1, b1, a2, b2)
    draw_line(c1, d1, c2, d2)

    set_stroke_width(1)
    red_fine = green_fine = blue_fine = alpha_fine = fine
    # r, g, b, alpha = RED, GREEN, BLUE, 0
    for i in range(number_of_strings + 1):
        x1 = x1_intervals[i]
        y1 = y1_intervals[i]
        x2 = x2_intervals[i]
        y2 = y2_intervals[i]
        set_stroke_color(re, gr, bl, alpha)
        draw_line(x1, y1, x2, y2)
        if re <= 0 or re <= 1:
            if re <= 0:
                re = 0 + 2 * abs(red_fine)
            elif re >= 1:
                re = 1 - 2 * abs(red_fine)
            red_fine = 0 - red_fine
        if gr <= 0 or g >= 1:
            if gr <= 0:
                gr = 0 + 2 * abs(green_fine)
            if gr >= 1:
                gr = 1 - 2 * abs(green_fine)
            green_fine = 0 - green_fine
        if bl <= 0 or b >= 1:
            if bl <= 0:
                bl = 0 + 2 * abs(red_fine)
            elif bl >= 1:
                bl = 1 - 2 * abs(red_fine)
            blue_fine = 0 - blue_fine
        if alpha <= 0 or alpha >= 1:
            if alpha <= 0:
                alpha = 0 + 2 * abs(alpha_fine)
            elif alpha >= 1:
                alpha = 1 - 2 * abs(alpha_fine)
            alpha_fine = 0 - alpha_fine
        re += red_fine
        gr -= green_fine
        bl += blue_fine
        alpha += alpha_fine
        # print(red_fine, green_fine, blue_fine, fine)


# Parameter-less function to call the draw function
# a, b, c, d, e, f, g, h = 25, 50, 50, 200, 350, 180, 200, 350
a, b, c, d, e, f, g, h = 25, 50, 50, 200, 750, 480, 600, 550
# a_factor, b_factor, c_factor, d_factor, e_factor, f_factor, g_factor, h_factor = 4, -4, -4, 4, -4, 4, 4, -4
# a_factor = random.randint(-100, 100)/1000
# b_factor = random.randint(-100, 100)/1000
# c_factor = random.randint(-100, 100)/1000
# d_factor = random.randint(-100, 100)/1000
# e_factor = random.randint(-100, 100)/1000
# f_factor = random.randint(-100, 100)/1000
# g_factor = random.randint(-100, 100)/1000
# h_factor = random.randint(-100, 100)/1000
#
# print(a_factor, b_factor, c_factor, d_factor, e_factor, f_factor, g_factor, h_factor)
def main():
    # draw(25, 50, 50, 200, 350, 180, 200, 350, 25)
    # draw(25, 50, 50, 200, 350, 180, 200, 350, 25)
    # while True
    global a2_factor, b2_factor, c2_factor, d2_factor, e2_factor, f2_factor, g2_factor, h2_factor
    global a, b, c, d, e, f, g, h, A
    global a_factor, b_factor, c_factor, d_factor, e_factor, f_factor, g_factor, h_factor
    global RED, GREEN, BLUE, red_step, green_step, blue_step, alpha_step
    global red_fine, green_fine, blue_fine, strings
    global re, gr, bl, alpha
    global fine, dimension1, dimension2

    # a_factor = random.randint(-100, 100) / 1000
    # b_factor = random.randint(-100, 100) / 1000
    # c_factor = random.randint(-100, 100) / 1000
    # d_factor = random.randint(-100, 100) / 1000
    # e_factor = random.randint(-100, 100) / 1000
    # f_factor = random.randint(-100, 100) / 1000
    # g_factor = random.randint(-100, 100) / 1000
    # h_factor = random.randint(-100, 100) / 1000

    if a_factor <= 0 or a_factor >= 1:
        a2_factor = 0 - a2_factor
    if b_factor <= 0 or b_factor >= 1:
        b2_factor = 0 - b2_factor
    if c_factor <= 0 or c_factor >= 1:
        c2_factor = 0 - c2_factor
    if d_factor <= 0 or d_factor >= 1:
        d2_factor = 0 - d2_factor
    if e_factor <= 0 or e_factor >= 1:
        e2_factor = 0 - e2_factor
    if f_factor <= 0 or f_factor >= 1:
        f2_factor = 0 - f2_factor
    if g_factor <= 0 or g_factor >= 1:
        g2_factor = 0 - g2_factor
    a_factor += a2_factor
    b_factor += b2_factor
    c_factor += c2_factor
    d_factor += d2_factor
    e_factor += e2_factor
    f_factor += f2_factor
    g_factor += g2_factor
    h_factor += h2_factor
    # if b_factor <= 0 or b_factor >= 1:
    #     b2_factor = 0 - b2_factor
    print(a_factor, b_factor, c_factor, d_factor, e_factor, f_factor, g_factor, h_factor)

    # draw(a, b, c, d, e, f, g, h, 25)
    if a not in dimension:
        a_factor = 0 - a_factor
    if b not in dimension1:
        b_factor = 0 - b_factor
    if c not in dimension:
        c_factor = 0 - c_factor
    if d not in dimension1:
        d_factor = 0 - d_factor
    if e not in dimension:
        e_factor = 0 - e_factor
    if f not in dimension2:
        f_factor = 0 - f_factor
    if g not in dimension:
        g_factor = 0 - g_factor
    if h not in dimension2:
        h_factor = 0 - h_factor
    a += a_factor
    b += b_factor
    c += c_factor
    d += d_factor
    e += e_factor
    f += f_factor
    g += g_factor
    h += h_factor

    fine = 1 / strings
    # print(red_fine, green_fine, blue_fine)
    if RED <= 0 or RED >= 1:
        if RED <= 0:
            RED = 2 * abs(red_step)
        elif RED >= 1:
            RED = 1 - 2 * abs(red_step)
        red_step = 0 - red_step
        # print("r:", red_step, "g:", green_step, "b:", blue_step)
    if GREEN <= 0 or GREEN >= 1:
        if GREEN <= 0:
            GREEN = 2 * abs(green_step)
        elif GREEN >= 1:
            GREEN = 1 - 2 * abs(green_step)
        green_step = 0 - green_step
        # print("r:", red_step, "g:", green_step, "b:", blue_step)
    if BLUE <= 0 or BLUE >= 1:
        if BLUE <= 0:
            BLUE = 2 * abs(blue_step)
        elif BLUE >= 1:
            BLUE = 1 - 2 * abs(blue_step)
        blue_step = 0 - blue_step
    if A <= 0 or A >= 1:
        if A <= 0:
            A = 2 * abs(alpha_step)
        elif A >= 1:
            A = 1 - 2 * abs(alpha_step)
        alpha_step = 0 - alpha_step
        # print("r:", red_step, "g:", green_step, "b:", blue_step)
    RED += red_step
    GREEN -= green_step
    BLUE += blue_step
    A += alpha_step
    re, gr, bl, alpha = RED, GREEN, BLUE, A
    draw(a, b, c, d, e, f, g, h, strings)
    # draw(25, 50, 50, 200, 350, 180, 200, 350, 250)
    # draw(25, 50, 50, 200, 350, 180, 200, 350, 25)


start_time = time.time()
start_graphics(main, title="String Art", width=WINDOW_WIDTH[0], height=WINDOW_WIDTH[1])

