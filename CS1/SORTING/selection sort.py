

import random


def selection_sort(list_of_values):
    n = len(list_of_values)

    # Loop over list items:
    for current_index in range(n):

        # Loop over items after current item in the list:
        for second_index in range(current_index, n):

            # Compare current item to second item. if current item is greater...
            if list_of_values[current_index] > list_of_values[second_index]:

                # SWAP ITEMS!
                list_of_values[current_index], list_of_values[second_index] = list_of_values[second_index], list_of_values[current_index]
    return list_of_values


while True:
    new_list = []
    n = int(input("How many items in the list? "))
    for index in range(n):
        new_list.append(random.randint(1, 100))
    print(f"Original list: {new_list}")
    print(f"Sorted list: {selection_sort(new_list)}")
