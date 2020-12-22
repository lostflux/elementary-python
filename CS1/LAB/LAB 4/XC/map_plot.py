# File Name: map_plot.py
# Author: Amittai Joel Wekesa
# Date: November 14, 2020
# Purpose: Code to map and plot the vertices.

# Imports:
from cs1lib import *
from load_graph import load_graph
from bfs import bfs


# Defining useful variables to be used in coordinating the functions:
vertex_dict = load_graph("dartmouth_graph.txt")  # Vertex dictionary
dartmouth_map = load_image("dartmouth_map.png")  # Map of Dartmouth
IMAGE_WIDTH = 1012
IMAGE_HEIGHT = 811
WINDOW_TITLE = "MAP OF DARTMOUTH"

# Global variables for the functions:
start_vertex = None
goal_vertex = None
path_used = None


# Function to detect mouse press and set start vertex:
def mouse_press(mx, my):
    global start_vertex, vertex_dict
    for key, vertex in vertex_dict.items():
        if vertex.mouse_in_range(mx, my):
            start_vertex = vertex


# Function to track mouse position and update goal vertex:
def mouse_move(mx, my):
    global goal_vertex, vertex_dict
    for key, vertex in vertex_dict.items():
        if vertex.mouse_in_range(mx, my):
            goal_vertex = vertex


# Function to call breadth-first search on the currently selected start and goal vertices:
def search():
    global path_used, start_vertex, goal_vertex, vertex_dict

    # Resetting the backpointers for all the vertices in vertex_dict
    for key, vertex in vertex_dict.items():
        vertex.backpointer = None

    # Find shortest path by calling bfs on the start vertex and goal vertex
    path_used, items_in_frontier, searched_items = bfs(start_vertex, goal_vertex)
    # print(frontier)
    return path_used, items_in_frontier, searched_items


# Function to draw map, vertices, and path:
def draw():
    global path_used
    draw_image(dartmouth_map, 0, 0)
    set_stroke_width(15)
    if start_vertex is not None and goal_vertex is not None:
        path_used, items_in_frontier, searched_items = search()
    else:
        items_in_frontier, searched_items = None, None
    for key, vertex in vertex_dict.items():
        vertex.draw_connections(path_used=path_used, frontier=items_in_frontier)
    for key, vertex in vertex_dict.items():
        if vertex == start_vertex or vertex == goal_vertex:
            if vertex == start_vertex:
                vertex.draw_point(255/255, 153/255, 51/255)
            elif vertex == goal_vertex:
                vertex.draw_point(0, 1, 0)
            vertex_name = vertex.name
            vertex_x = vertex.x
            vertex_y = vertex.y + 30
            set_font_size(15)
            set_stroke_color(1, 0.4, 1)
            draw_text(vertex_name, vertex_x, vertex_y)
        elif path_used is not None and vertex in path_used:
            vertex.draw_point(1, 0, 0)
        elif items_in_frontier is not None and vertex in items_in_frontier:
            vertex.draw_point(28/255, 154/255, 228/255)
        elif searched_items is not None and vertex in searched_items:
            print([searched_item.name for searched_item in searched_items])
            vertex.draw_point(1, 1, 0)
        else:
            vertex.draw_point(0, 0, 1)


start_graphics(draw, title=WINDOW_TITLE, width=IMAGE_WIDTH,
               height=IMAGE_HEIGHT, mouse_press=mouse_press,
               mouse_move=mouse_move)
