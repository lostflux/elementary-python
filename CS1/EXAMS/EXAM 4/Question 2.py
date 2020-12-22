# File Name: Question 1.py
# Author: Amittai Joel Siavava Wekesa
# Date: November 6, 2020
# Purpose: EXAM 4 Question 2 -- Recursion


# Function to find if str1 is a suffix of str2:
def find_suffix(str1, str2, index1=0):
    # Empty string is subset of all other strings
    if len(str1) == 0:
        return True

    # A longer string cannot be a suffix of a shorter string:
    # Note that this also takes care of cases where len(str1) > 0 and len(str2) == 0
    elif len(str1) > len(str2):
        return False

    # OR ELSE, do...
    else:
        # Let index1 be the start position in str1
        # Let index2 be the start position in str2

        index2 = len(str2) - (len(str1) - index1)
        equality_check = str1[index1] == str2[index2]

        # if index1 is the index of last letter in str1,
        # return the equality check
        if index1 == len(str1) - 1:
            return equality_check

        # if index1 is not last index in str1,
        # return status check compared with recursive call of next index
        else:
            return equality_check and find_suffix(str1, str2, index1 + 1)


# Test cases:
string1, string2 = "washer", "dishwasher"
print(find_suffix(string1, string2))

string3, string4 = "wash", "dishwasher"
print(find_suffix(string3, string4))

string5, string6 = "", "test"
print(find_suffix(string5, string6))

string7, string8 = "test", ""
print(find_suffix(string7, string8))

string9, string10 = "", ""
print(find_suffix(string9, string10))

string11, string12 = "test", "test"
print(find_suffix(string11, string12))
