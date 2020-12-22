# File Name: quicksort.py
# Author: Amittai Joel Wekesa
# Date: November 07, 2020
# Purpose: partition, quick_sort, and sort functions


# partition function:
def partition(list_of_values, p, r, compare_func):
    # n = len(list_of_values)
    pivot = list_of_values[r]
    i = p - 1
    for j in range(p, r):
        if compare_func(list_of_values[j], pivot):
            i += 1
            list_of_values[i], list_of_values[j] = list_of_values[j], list_of_values[i]
            j += 1
        else:
            j += 1

        if not compare_func(list_of_values[j - 1], pivot):
            j -= 1
        if j == r:
            break

    list_of_values[i + 1], list_of_values[r] = list_of_values[r], list_of_values[i + 1]
    # print(list_of_values)
    return i + 1


# quick_sort function
def quick_sort(list_of_values, p, r, compare_func):
    if len(list_of_values[p:r + 1]) < 2:
        return list_of_values
    else:
        q = partition(list_of_values, p, r, compare_func)

        quick_sort(list_of_values, q + 1, r, compare_func)
        quick_sort(list_of_values, p, q - 1, compare_func)
        return list_of_values


# sort function
def sort(list_of_values, compare_func):
    p = 0
    r = len(list_of_values) - 1
    quick_sort(list_of_values, p, r, compare_func)
    return list_of_values




# new_list = [2, 8, 7, 1, 3, 5, 6, 4]
# new_list = [9, 8, 6, 7, 1, 3, 2, 4]
# n = len(new_list) - 1
# print(f"Old_list: {new_list}")
# print(f"Sorted list: {sort(new_list, compare_func)}")
