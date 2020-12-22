# File Name: Question 1.py
# Author: Amittai Joel Siavava Wekesa
# Date: November 6, 2020
# Purpose: EXAM 4 Question 3 -- Recursion


# Function to return sliced list [m:n]:
def slice_list(glist, m, n):

    # Check if end point is out of list and set it to the length of list
    if n > len(glist):
        n = len(glist)

    # Check if start index is >= end index and return empty list
    if m >= n:
        return []

    # Or else:
    else:

        # Find results list from next recursive call and append the current element
        results_list = slice_list(glist, m, n-1)
        results_list.append(glist[n-1])
        return results_list


# Test cases:
list_1 = [10, 2, 4, 23, 3, 2, 7]
list_2 = []


# Cases from exam question
print(f"Case 1: {slice_list(list_1, 2, 4)}")

print(f"Case 2: {slice_list(list_1, 3, 10)}")

print(f"Case 3: {slice_list(list_1, 2, 2)}")

print(f"Case 4: {slice_list(list_1, 9, 11)}")

print(f"Case 5: {slice_list(list_2, 1, 2)}")
