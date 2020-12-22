# File Name: load_graph.py
# Author: Amittai Joel Wekesa
# Date: November 10, 2020
# Purpose: Loading graph vertices from text file.

# Imports:
from vertex import *


# Function to split lines:
def parse_line(line):
    section_split = line.split(";")
    vertex_name = section_split[0].strip()

    adjacent_vertices = section_split[1].strip().split(",")

    # add all except empty strings
    adjacent = []
    for a in adjacent_vertices:
        if a:
            adjacent.append(a.strip())

    x = section_split[2].split(",")[0].strip()
    y = section_split[2].split(",")[1].strip()

    return vertex_name, adjacent, x, y


# Function to load graph:
def load_graph(text_file):
    text_data = open(text_file, "r")
    vertex_dict = {}
    for line in text_data:
        if len(line.split(";")) == 3:
            vertex_name, neighbors, x, y = parse_line(line)
            vertex_dict[vertex_name] = Vertex(vertex_name, x, y)
    text_data.close()

    text_data = open(text_file, "r")
    for line in text_data:
        if len(line.split(";")) == 3:
            vertex_name, neighbors, x, y = parse_line(line)
            for adjacent_vertex in neighbors:
                vertex_dict[vertex_name].adjacency_list.append(vertex_dict[adjacent_vertex])
                # print(vertex_name, adjacent_vertex)
    text_data.close()

    return vertex_dict
