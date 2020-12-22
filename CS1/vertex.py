# File Name: vertex.py
# Author: Amittai Joel Wekesa
# Date: November 07, 2020
# Purpose: Vertex class


# Imports
from cs1lib import *

# Defining constants:
POINT_SIZE = 1


# Vertex class:
class Vertex:
    def __init__(self, name, x, y):
        self.name = name
        self.x = int(x)
        self.y = int(y)
        self.adjacency_list = []

    def __str__(self):
        adjacents = ""
        for index in range(len(self.adjacency_list)):
            if index != 0:
                adjacents += ", "
            adjacents += self.adjacency_list[index].name

        return f"{self.name}; Location: {self.x}, {self.y}; Adjacent vertices: {adjacents}"

    def draw_point(self, r=1, g=0, b=0):
        x = self.x
        y = self.y
        enable_stroke()
        enable_fill()
        set_stroke_color(r, g, b)
        set_fill_color(r, g, b)
        set_stroke_width(10)
        draw_circle(x, y, POINT_SIZE)
        disable_fill()

    def draw_connections(self, r=0, g=0, b=1):
        x1 = self.x
        y1 = self.y
        set_stroke_color(r, g, b)
        set_stroke_width(5)
        for adjacent_vertex in self.adjacency_list:
            x2 = adjacent_vertex.x
            y2 = adjacent_vertex.y
            draw_line(x1, y1, x2, y2)
