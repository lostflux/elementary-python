# File Name: node.py
# Purpose: Node class for EXAM 5


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def set_next(self, node):
        self.next = node
