# FileName: Question 1.py
# Author: Amittai Joel Wekesa
# Date: December 01, 2020
# Purpose: EXAM 5 Question 2

# Imports:
from node import Node
from helpers import *


# Function to create linked list containing passed data in reversed order:
def reversed_ll(glist):
    if len(glist) == 0:
        head = None

    else:
        next_node = Node(glist[0])
        current_index = 1
        while current_index <= len(glist) - 1:
            current_node = Node(glist[current_index])
            current_node.next = next_node
            next_node = current_node
            current_index += 1
        head = current_node  # Setting the head to be the node of last item in list
    return head


# Driver code
list_of_values = []
raw_list = input("Enter numbers separated by commas: ").split()
if len(raw_list) == 0:
    list_of_values = []
else:
    for i in raw_list:
        try:
            list_of_values.append(int(i))
        except:
            print(i, "is not a valid number")
            continue

start_node = reversed_ll(list_of_values)
if start_node is None:
    print("start_node is None")
else:
    print_ll(start_node)
    print(start_node.data)

