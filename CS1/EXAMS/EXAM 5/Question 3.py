# FileName: Question 1.py
# Author: Amittai Joel Wekesa
# Date: December 01, 2020
# Purpose: EXAM 5 Question 3


# Function to calculate average of values in dictionary
# And print names of students who scored above teh average:
def analyze_dict(givend):
    count, total_sum = 0, 0
    for value in givend.values():
        total_sum += value
        count += 1

    average = total_sum/count
    for key, value in givend.items():
        if value > average:
            print(key)

    return average


# Examples from Exam question
list1 = {"Vasanta": 20, "Mary": 50, "John": 40 }
print(analyze_dict(list1))

list2 = {"Vasanta": 20, "Mary": 50, "John": 40, "Priti": 50}
print(analyze_dict(list2))

list3 = {"Vasanta": 20}
print(analyze_dict(list3))
