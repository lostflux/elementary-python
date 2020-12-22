# File Name : Question 4.py
# Author    : AMITTAI JOEL SIAVAVA WEKESA
# Date      : October 09, 2020
# Purpose   : Exam 2, Question 4

# Imports
import random

# Function to find and PRINT indices of 2 inner lists with most common elements:
def check_lists(glol):
    max_count = 0
    index_1, index_2 = None, None
    for mini_list in glol:
        for second_list_index in range(glol.index(mini_list) + 1, len(glol)):
            counter = 0
            second_list = glol[second_list_index]
            for element in mini_list:
                if element in second_list:
                    counter += 1
            if counter > max_count:
                max_count = counter
                index_1, index_2 = glol.index(mini_list), glol.index(second_list)

    # In case all the mini-lists don't have any common elements:
    if index_1 is None:
        # Printing first element and any other element in list
        index_1 = 0
        index_2 = random.randint(1, len(glol) - 1)
    print(index_1, index_2)


# Example tests from the EXAM Question
list1 = [[10, 4, 30], [7, 8, 4, 11], [9, 4, 3, 7], [11, 7, 4, 1]]
list2 = [[10, 4, 30], [7, 8, 4, 10], [11, 7, 4, 1]]
list3 = [[10, 4, 30], [7, 8, 40], [11, 1], [23], [ ]]

check_lists(list1)
check_lists(list2)
check_lists(list3)

