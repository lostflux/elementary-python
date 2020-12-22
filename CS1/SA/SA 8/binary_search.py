# binary_search.py
# Code provided for CS 1 Short Assignment 7.
# Performs binary search on a sorted list of random numbers.

from random import randint
import math


# Perform binary search for key on the sublist of the_list
# starting at index left and going up to and including index right.
# If key appears in the_list, return the index where it appears.
# Otherwise, return None.
# Requires the_list to be sorted.

def binary_search(the_list, key, left=None, right=None):
    # If using the default parameters, then search the entire list.
    if left is None and right is None:
        left = 0
        right = len(the_list) - 1

    # YOU FILL IN THE REST OF THIS FUNCTION.

    # Check if the list slice is empty and return "None"
    if len(the_list[left:right + 1]) == 0:
        return None

    # If list slice not empty then:
    else:
        # Find midpoint. If even elements e.g. [0, 1, 2, 3], return index of 1 not 2
        mid_point = (left + right) // 2  # Find midpoint. If even elements e.g. [0, 1, 2, 3], return index of 1 not 2

        # If middle element is equal to the key, return the index of middle element
        if key == the_list[mid_point]:
            return mid_point

        # Else run binary_search on the elements BEFORE middle element if middle element > key
        elif key < the_list[mid_point]:
            return binary_search(the_list, key, left, mid_point - 1)

        # Else run binary_search on the elements AFTER middle element if middle element < key
        else:
            return binary_search(the_list, key, mid_point + 1, right)


# Driver code for binary search.
n = int(input("How many items in the list? "))

# Make a list of n random ints.
i = 0
the_list = []
while i < n:
    the_list.append(randint(0, 1000))
    i += 1

# Binary search wants a sorted list.
the_list = sorted(the_list)
print("The list: " + str(the_list))

while True:
    key = input("What value to search for? ('?' to see the list, 'q' to quit): ")

    if key == "?":
        print("The list: " + str(the_list))
    elif key == "q":
        break
    else:
        key = int(key)
        index = binary_search(the_list, key)
        if index == None:
            print(str(key) + " not found")
        else:
            print(str(key) + " found at index " + str(index))