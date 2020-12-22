# File Name : Question 2.py
# Author    : AMITTAI JOEL SIAVAVA WEKESA
# Date      : October 09, 2020
# Purpose   : Exam 2, Question 2

# Function to separate integer elements in a list by even or odd:
def separate_list(glist):
    separated_list = [[], []]
    for element in glist:
        if element % 2 == 0:
            separated_list[0].append(element)
        elif element % 2 == 1:  # Avoided using "else" in case of non-integers
            separated_list[1].append(element)

    return separated_list


# Initializing inputs and calling the function
while True:
    list_of_values = map(int, input("Enter list values separated by spaces: ").split())
    print(separate_list(list_of_values))

# # Sample tests from the exam Question
# list1 = [99, 34, 56, 33, 1, 6]
# list2 = [5, 7, 3, 15]
# list3 = [6, 4, 2, 8, 16]
# list4 = []
#
# print(separate_list(list1))
# print(separate_list(list2))
# print(separate_list(list3))
# print(separate_list(list4))
