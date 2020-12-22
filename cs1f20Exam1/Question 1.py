# Author: AMITTAI JOEL WEKESA
# Date: 25/09/2020
# Purpose: Exam 1, Question 1 -- Checking for odd numbers.

# Function to check if a number is odd
def is_odd(n):
    odd_status = (n % 2) == 1
    print(odd_status)


# Initializing the input values and calling the function
n = int(input("Enter a number to check if it is odd: "))
is_odd(n)
