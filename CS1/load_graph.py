# File Name: load_graph.py
# Author: Amittai Joel Wekesa
# Date: November 10, 2020
# Purpose: Loading graph vertices from text file.

# Imports:
from vertex import *


# Function to load graph:
def load_graph(text_file):
    text_data = open(text_file, "r")
    vertex_dict = {}
    for line in text_data:
        line_elements = line.split(";")
        if len(line_elements) == 3:
            vertex_name, neighbors, x, y = map(line_elements)
            vertex_dict[vertex_name] = Vertex(vertex_name, x, y)

    for line in text_data:
        line_elements = line.split(";")
        if len(line_elements) == 3:
            vertex_name = line_elements[0]
            adjacent_vertices = line_elements[1]
            for adjacent_vertex in adjacent_vertices.split(","):
                vertex_dict[vertex_name].adjacency_list.append(vertex_dict[adjacent_vertex])

    return vertex_dict
