# File Name : Question 3.py
# Author    : AMITTAI JOEL SIAVAVA WEKESA
# Date      : October 09, 2020
# Purpose   : Exam 2, Question 3

# Function to check if one string is a subset of another:
def check_subsets(s1, s2):
    # Assuming s1 is shorter than s2:
    S1_LENGTH, S2_LENGTH = len(s1), len(s2)
    status = False
    if len(s1) == 0:
        status = True  # Empty first string is subset of all other strings.
    elif len(s2) == 0:
        status = False  # Empty second string can't have a non-empty subset.
    else:
        start_range = (S2_LENGTH - S1_LENGTH) + 1
        for index in range(start_range):
            if s2[index: index + S1_LENGTH] == s1:
                status = True
                break
    return status


# Initializing inputs and calling the function
while True:
    s1 = input("Enter s1 (shorter string): ")
    s2 = input("Enter s2 (longer string): ")
    print(check_subsets(s1, s2))
