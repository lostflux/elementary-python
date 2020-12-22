# File Name: counter.py
# Author: AMITTAI JOEL SIAVAVA WEKESA
# Date: 14th October, 2020
# Purpose: SA 6 -- Counter class

# Creating the Counter class:
class Counter:

    def __init__(self, limit, initial=0, min_digits=1):
        self.limit = limit
        if initial in range(0, limit - 1):
            self.current_value = initial
        else:
            print(f"""\nError! Initial value out of range. \nChanged initial value from {initial} to {limit-1} \n""")
            self.current_value = limit - 1
        self.min_digits = min_digits

    def get_value(self):
        return int(self.current_value)

    def __str__(self):
        string_value = str(self.current_value)
        string_value = "0" * (self.min_digits - len(string_value)) + string_value
        return string_value

    def tick(self):
        if self.current_value == 0:
            self.current_value = self.limit - 1
            return True
        else:
            self.current_value -= 1
            return False

# a = Counter(60, 0, 1)
# a.tick()
# b = Counter(70, 0, 1)
# b.tick()
# print(a.get_value() + b.get_value())
