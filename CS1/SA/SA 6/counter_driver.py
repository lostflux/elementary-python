# File Name: counter_driver.py
# Author: AMITTAI JOEL SIAVAVA WEKESA
# Date: 14th October, 2020
# Purpose: SA 6 -- Counter driver

# Imports:
from counter import Counter

# Creating two Counter objects
a = Counter(60)
b = Counter(10, initial=200, min_digits=3)

# Printed the object call for easy reference:
print("b = Counter(10, initial=5, min_digits=3)")

# Checking the type of object b:
print(f"type of b: {type(b)}")

# Checking the integer current_value of object b:
print(f"b.get_value(): {b.get_value()}")

# Checking the type of the integer current_value (should be <class 'int'>):
print(f"type of b.get_value: {type(b.get_value())}")

# Checking the current_value, type, and length of current_value returned by the __str__ class
print(f"b.__str__: {b.__str__()}")
print(f"type of b.__str__ : {type(b.__str__())}")
print(f"length of b.__str__ : {len(b.__str__())}")

# Creating a list of tick values and appending
# consecutive tick values to the list:
tick_values = []
for i in range(15):
    tick_values.append(b.get_value())
    b.tick()
print(f"Consecutive ticks: {tick_values}")
