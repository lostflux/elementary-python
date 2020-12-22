# File Name: vertex.py
# Author: Amittai Joel Wekesa
# Date: November 07, 2020
# Purpose: Vertex class


# Imports
from cs1lib import *

# Defining constants:
POINT_SIZE = 5
EDGE_WIDTH = 5


# Vertex class:
class Vertex:
    def __init__(self, name, x, y):
        self.name = name
        self.x = int(x)
        self.y = int(y)
        self.adjacency_list = []
        self.backpointer = None

    def __str__(self):
        adjacent_vertices = ""
        for index in range(len(self.adjacency_list)):
            if index != 0:
                adjacent_vertices += ", "
            adjacent_vertices += self.adjacency_list[index].name
        return f"{self.name}; Location: {self.x}, {self.y}; Adjacent vertices: {adjacent_vertices}"

    def draw_point(self, r=0, g=0, b=1):
        x = self.x
        y = self.y
        enable_stroke()
        enable_fill()
        set_stroke_color(r, g, b)
        set_fill_color(r, g, b)
        draw_circle(x, y, POINT_SIZE)
        disable_fill()

    def draw_connections(self, r=0, g=0, b=1, path_used=None):
        x1 = self.x
        y1 = self.y
        set_stroke_color(r, g, b)
        set_stroke_width(EDGE_WIDTH)
        for adjacent_vertex in self.adjacency_list:
            x2 = adjacent_vertex.x
            y2 = adjacent_vertex.y
            if path_used is not None and self in path_used and adjacent_vertex in path_used:
                set_stroke_color(1, 0, 0)
            else:
                set_stroke_color(0, 0, 1)
            draw_line(x1, y1, x2, y2)

    def mouse_in_range(self, mx, my):
        return self.x - POINT_SIZE <= mx <= self.x + POINT_SIZE and self.y - POINT_SIZE <= my <= self.y + POINT_SIZE
