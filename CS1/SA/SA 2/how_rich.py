# Author: AMITTAI JOEL SIAVAVA WEKESA
# Date: 09/19/2020
# Purpose: SA 2 Problem 1 -- Using Loops to compute a compounded current_value over multiple years.
# Note: I was studying for-loops and decided to include an alternate solution using a for-loop.

# Initializing constants:
BRUTUS_INITIAL_DEPOSIT = 1.00
BRUTUS_INTEREST_RATE = 5
DEPOSIT_YEAR = 0
CURRENT_YEAR = 2020

# Initializing Variables to be used in computation:
value_in_bank = value_in_bank_2 = BRUTUS_INITIAL_DEPOSIT
year = DEPOSIT_YEAR

# While Loop to compute compounded current_value
while year < CURRENT_YEAR:
    value_in_bank *= (1 + BRUTUS_INTEREST_RATE / 100)
    year += 1

# Printing the current_value:
print("The compounded current_value in 2020 is:", value_in_bank)

