# File Name: Question 1.py
# Author: Amittai Joel Siavava Wekesa
# Date: November 6, 2020
# Purpose: EXAM 4 Question 1 -- Recursion


# Function to find product of odds less or equal to a number
def product_of_odds(n):

    # Base case where n is 1, return 1  -- or n itself:
    if n == 1:
        return n

    # if n is even, return the recursive call on n - 1
    elif n % 2 == 0:
        return product_of_odds(n - 1)
    # if n is odd, return n times recursive call on n - 2, the next odd number:
    else:
        return n * product_of_odds(n - 2)

# Test cases from question:
a1 = 7
print(product_of_odds(a1))
a2 = 6
print(product_of_odds(a2))
