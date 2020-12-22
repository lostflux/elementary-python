# File Name : Question 5.py
# Author    : AMITTAI JOEL SIAVAVA WEKESA
# Date      : October 09, 2020
# Purpose   : Exam 2, Question 5

# Function to check missing recurrence of elements in mini-lists within a list
# Print true ONLY if each element in a mini-list misses only 1 other mini_list
def missing_element(glol):
    status = False
    for mini_list in glol:
        for element in mini_list:
            missing_counter = 0
            for second_list in glol:
                # Skipping comparing mini_list to itself
                if glol.index(mini_list) == glol.index(second_list):
                    continue

                # Check if element from mini_list is not in second_list:
                elif element not in second_list:
                    missing_counter += 1

            # If element's missing recurrence is 1, continue checking other elements.
            status = missing_counter == 1
            if status:
                continue

            # else if element's missing recurrence is not 1, return "False" and exit.
            else:
                return status

    # Finally, if all elements miss only once (status == "True")
    # or lists are empty (status == "False")
    # return the status
    return status


# Example tests from the EXAM Question:
list1 = [[4, 76, 32, 45], [4, 45], [76, 32, 4], [45, 32, 76]]
list2 = [[40, 7, 3, 4], []]
list3 = [[8, 11], [8, 3, 5], [3, 5]]
list4 = [[8, 11, 3], [8, 3, 5], [3, 5]]

print(missing_element(list1))
print(missing_element(list2))
print(missing_element(list3))
print(missing_element(list4))
