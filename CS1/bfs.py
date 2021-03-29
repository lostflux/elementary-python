# File Name: bfs.py
# Author: Amittai Joel Wekesa
# Date: November 14, 2020
# Purpose: Breadth-First Search

# Imports:
from collections import deque


# Function to perform breadth-first search:
def bfs(start_vertex, goal_vertex, path=None, path_length=0):
    if path is None:
        path = deque()
    path_length += 1
    for next_vertex in start_vertex.adjacency_list:
        if next_vertex == goal_vertex:
            path.append(next_vertex)
            return path, path_length
        else:
            return bfs(next_vertex, goal_vertex, path, path_length)
