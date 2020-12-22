# FileName: Question 1.py
# Author: Amittai Joel Wekesa
# Date: December 01, 2020
# Purpose: EXAM 5 Question 4


# Function to return intersection of two lists:
def intersection(glist1, glist2):
    intersection_dict = {}
    intersection_list = []
    dict1 = {}
    for item in glist1:  # Item in list = O(n1)
        dict1[item] = 1

    for num in glist2:  # Item in list = O(n2)
        if num in dict1:
            intersection_dict[num] = 1

    for num in intersection_dict:  # Dictionary lookup = O(1)
        intersection_list.append(num)
    return intersection_list


# Examples from exam question:
list1 = [10, 30, 20, 10]
list2 = [10, 40, 40, 20, 5, 4]
print(intersection(list1, list2))

list3 = []
list4 = [10, 40, 40, 20]
print(intersection(list3, list4))

list5 = [10, 30, 4, 20, 10, 5]
list6 = []
print(intersection(list5, list6))

list7 = [10, 30, 20, 10]
list8 = [30, 10, 20, 30, 10]
print(intersection(list7, list8))
