# Author: AMITTAI JOEL WEKESA
# Date: 25/09/2020
# Purpose: Exam 1, Question 6 -- Checking the commonality of factors.

# Function to print "True" if m and n have only 2 common factors
def number_of_factors(m, n):
    current_integer = 1
    count_of_factors = 0
    if m < n:
        bound = m
    else:
        bound = n
    while current_integer <= bound:
        if m % current_integer == 0 and n % current_integer == 0:
            count_of_factors += 1
        current_integer += 1
    status_check = count_of_factors == 2
    print(status_check)


m = int(input("Enter first number: "))
n = int(input("Enter the second number: "))
number_of_factors(m, n)
