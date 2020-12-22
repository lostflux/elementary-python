# Author: AMITTAI JOEL WEKESA
# Date: 25/09/2020
# Purpose: Exam 1, Question 3 -- Finding all positive factors of a number.


# Function to find all positive factors of a number.
def factors(n):
    current_int = 1
    while current_int <= n:
        if n % current_int == 0:
            print(current_int)
        current_int += 1


# Initializing input values and calling the function
x = int(input("Enter a number: "))
factors(x)
