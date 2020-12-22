# Author: AMITTAI JOEL WEKESA
# Date: 25/09/2020
# Purpose: Exam 1, Question 4 -- Finding the k smallest multiples of m and n.


# Function to find k multiples of m and n
def multiples(m, n, k):
    counter = 0
    if m < n:
        current_integer = n
    else:
        current_integer = m
    while counter < k:
        if current_integer % m == 0 and current_integer % n == 0:
            print(current_integer)
            counter += 1
        current_integer += 1


# Initializing inputs and calling the function
m = int(input("Enter the current_value of m: "))
n = int(input("Enter the current_value of n: "))
k = int(input("Enter the current_value of k: "))
multiples(m, n, k)
