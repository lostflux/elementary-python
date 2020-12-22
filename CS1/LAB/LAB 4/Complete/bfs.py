# File Name: bfs.py
# Author: Amittai Joel Wekesa
# Date: November 14, 2020
# Purpose: Breadth-First Search

# Imports:
from collections import deque


# Function to perform breadth-first search:
def bfs(start_vertex, goal_vertex):
    # Create frontier list
    frontier = deque()
    frontier.append(start_vertex)

    # Perform BFS until goal_vertex is reached:
    while len(frontier) > 0:
        current_vertex = frontier.popleft()
        for next_vertex in current_vertex.adjacency_list:
            if next_vertex.backpointer is None:
                next_vertex.backpointer = current_vertex
                frontier.append(next_vertex)
                if next_vertex == goal_vertex:
                    break

    # Run through the back-chain and record the path:
    path_used = []
    check_vertex = goal_vertex
    while check_vertex != start_vertex:
        path_used.append(check_vertex)
        check_vertex = check_vertex.backpointer
    path_used.append(start_vertex)

    return path_used
