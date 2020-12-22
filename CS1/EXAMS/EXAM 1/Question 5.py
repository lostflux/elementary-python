# Author: AMITTAI JOEL WEKESA
# Date: 25/09/2020
# Purpose: Exam 1, Question 5 -- Finding the occurrence of fibonacci...
# ... numbers between m and n.


# Function to check for fibonacci numbers between a given range
def check_fibonacci(m, n):
    count = 0
    LOWER_BOUND = m
    UPPER_BOUND = n
    f1, f2 = 0, 1
    while f2 <= UPPER_BOUND:
        if LOWER_BOUND <= f2:
            count += 1

        # Calculating the consecutive values in the Fibonacci sequence
        # f1, f2 = f2, f1 + f2
        temp_variable = f1 + f2
        f1 = f2
        f2 = temp_variable

    print(count)


# Initializing input values and calling the function
m = int(input("Enter the lower bound: "))
n = int(input("Enter the upper bound: "))
check_fibonacci(m, n)
