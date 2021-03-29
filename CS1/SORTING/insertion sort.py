


import random


def insertion_sort(list_of_values):
    n = len(list_of_values)

    # Loop over indexes in the range of the list
    for current_index in range(1, n):

        # Remember value at current index
        key = list_of_values[current_index]

        # Start at the index directly before current item
        second_index = current_index - 1

        # Iterate second index all the way to 0... Compare with value at current index. If >,
        while second_index >= 0 and list_of_values[second_index] > key:

            # Slide item one to the right!
            list_of_values[second_index + 1] = list_of_values[second_index]
            second_index -= 1

        # Insert the key item to the created index
        list_of_values[second_index + 1] = key
        print(list_of_values)
    return list_of_values


new_list = [2, 5, 7, 9, 1, 4, 3, 8]
print(f"Original list: {new_list}")
print(f"Sorted list: {insertion_sort(new_list)}")
# while True:
#     new_list = []
#     n = int(input("How many items in the list? "))
#     for index in range(n):
#         new_list.append(random.randint(1, 100))
#     print(f"Original list: {new_list}")
#     print(f"Sorted list: {insertion_sort(new_list)}")
