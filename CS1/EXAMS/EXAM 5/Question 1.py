# FileName: Question 1.py
# Author: Amittai Joel Wekesa
# Date: December 01, 2020
# Purpose: EXAM 5 Question 1

# Imports:
from helpers import *


# Function to take reference to start node of a linked list
# And return data of last node:
def last_in_link(ghead):
    while ghead.next is not None:
        ghead = ghead.next
    return ghead.data


# Driver code
list_of_values = []
for i in input("Enter number separated by commas: ").split():
    try:
        list_of_values.append(int(i))
    except:
        print(i, "is not a valid number")
        continue

start_node = build_ll(list_of_values)
print_ll(start_node)
print(last_in_link(start_node))
