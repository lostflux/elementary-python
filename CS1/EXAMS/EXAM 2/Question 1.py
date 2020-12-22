# File Name : Question 1.py
# Author    : AMITTAI JOEL SIAVAVA WEKESA
# Date      : October 09, 2020
# Purpose   : Exam 2, Question 1

# Function to find the longest element in a list:
def longest_in_list(glist):
    longest_length = 0
    longest_index = None
    for element in glist:
        if len(element) >= longest_length:
            longest_length = len(element)
            longest_index = glist.index(element)
    return longest_index


# Sample tests from the Exam Question
list1 = ["test", "testing", "tested"]
list2 = ["test", "tested", "tester"]
list3 = ["test"]

print(longest_in_list(list1))
print(longest_in_list(list2))
print(longest_in_list(list3))

# Additional test
list4 = ["0", "01", "012", "0123", "01234"]
print(longest_in_list(list4))
