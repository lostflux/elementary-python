# File Name: counter.py
# Author: AMITTAI JOEL SIAVAVA WEKESA
# Date: 14th October, 2020
# Purpose: SA 6 -- Counter class

class Counter:

    def __init__(self, limit, initial=0, min_digits=1):
        self.limit = limit
        if initial in range(0, limit - 1):
            self.initial = initial
        else:
            print("Error! Initial current_value out of range.")
            self.initial = limit - 1
        self.min_digits = min_digits
        self.value = self.initial

    def get_value(self):
        return int(self.value)

    def __str__(self):
        string_value = str(self.value)
        string_value = "0" * (self.min_digits - len(string_value)) + string_value
        return string_value

    def tick(self):
        if self.value == 0:
            self.limit -= 1
            self.value = self.limit
            return True
        else:
            self.value -= 1
            return False
