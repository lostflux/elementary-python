# File Name: vertex.py
# Author: Amittai Joel Wekesa
# Date: November 07, 2020
# Purpose: Vertex class


# Vertex class:
class Vertex:
    def __init__(self, name, adjacent_vertices, data):
        self.name = name
        self.data = data
        self.adjacency_list = [vertex for vertex in adjacent_vertices]

    def __str__(self):
        return self.data
