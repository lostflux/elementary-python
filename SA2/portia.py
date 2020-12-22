# Author: AMITTAI JOEL SIAVAVA WEKESA
# Date: 09/19/2020
# Purpose: SA2 Problem 2 -- Using Loops to find year when Brutus's wealth surpassed Portia's.

# Initializing constants:
BRUTUS_INITIAL_DEPOSIT = 1.00
PORTIA_INITIAL_DEPOSIT = 100000
BRUTUS_INTEREST_RATE = 5
PORTIA_INTEREST_RATE = 4
DEPOSIT_YEAR = 0

# Initializing variables to be used:
year = DEPOSIT_YEAR
brutus_value = BRUTUS_INITIAL_DEPOSIT
portia_value = PORTIA_INITIAL_DEPOSIT
# brutus_rate = 1 + BRUTUS_INTEREST_RATE / 100
# portia_rate = 1 + PORTIA_INTEREST_RATE / 100

# While Loop to calculate values over the years:
while True:
    brutus_value *= 1 + BRUTUS_INTEREST_RATE / 100
    portia_value *= 1 + PORTIA_INTEREST_RATE / 100
    year += 1

    # If statement to compare values and determine if the condition is met
    # or the while loop should continue running
    if brutus_value > portia_value:
        print(f"Brutus's wealth surpassed Portia's wealth in the year {year}")
        print(f"Brutus's Wealth in {year} was: {brutus_value}")
        print(f"Portia's Wealth in {year} was: {portia_value}")
        break
