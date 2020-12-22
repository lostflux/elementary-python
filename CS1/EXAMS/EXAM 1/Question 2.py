# Author: AMITTAI JOEL WEKESA
# Date: 25/09/2020
# Purpose: Exam 1, Question 2 -- Printing all numbers in a given range in descending order.

# Function to print all numbers in a give range, descending order, inclusive of boundaries
def print_in_range(m, n):
    if m > n:
        UPPER_BOUND, LOWER_BOUND = m, n
    else:
        UPPER_BOUND, LOWER_BOUND = n, m

    current_value = UPPER_BOUND
    while current_value >= LOWER_BOUND:
        print(current_value)
        current_value -= 1


# Initializing input values and calling the function
m = int(input("Enter the first number: "))
n = int(input("Enter the second number: "))
print_in_range(m, n)
