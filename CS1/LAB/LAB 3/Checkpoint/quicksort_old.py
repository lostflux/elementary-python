
import random


def compare_func(list_of_values, pivot):
    n = len(list_of_values)
    for index in range(pivot):
        for second_index in range(pivot, n):
            if list_of_values[index] > list_of_values[second_index]:
                list_of_values[index], list_of_values[second_index] = list_of_values[second_index], list_of_values[index]
    return list_of_values


def partition(list_of_values, start, end, compare_func):
    pivot = (start + end) // 2
    print(len(list_of_values), pivot)
    return compare_func(list_of_values, pivot)


def quick_sort(list_of_values, start = None):
    pass




new_list = [2, 8, 7, 1, 3, 5, 6, 4]
n = len(new_list) + 1
print(f"Old_list: {new_list}")
print(f"Partitioned list: {partition(new_list, start=0, end=n, compare_func=compare_func)}")
# print(f"Pivot: {new_list[partition(new_list, end=n)]}")
# print(f"Sorted list: {quick_sort(new_list)}")