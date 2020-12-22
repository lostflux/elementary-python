# File Name: timer.py
# Author: AMITTAI JOEL SIAVAVA WEKESA
# Date: 11th October, 2020
# Purpose: SA 6 -- Timer class

# imports:
from counter import Counter

# Creating the Timer class:
class Timer:

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

        seconds_format, minutes_format, hours_format = 2, 2, 2

        self.hour_count = Counter(24, initial=self.hours, min_digits=hours_format)
        self.minute_count = Counter(60, initial=self.minutes, min_digits=minutes_format)
        self.second_count = Counter(60, initial=self.seconds, min_digits=seconds_format)

    def __str__(self):
        current_time = str(self.hour_count) + ":" + str(self.minute_count) + ":" + str(self.second_count)
        return current_time

    def tick(self):
        if self.second_count.tick():
            if self.minute_count.tick():
                self.hour_count.tick()

    def is_zero(self):
        return self.__str__() == "00:00:00"


# a = Timer(0, 0, 0)
# print(a)
# a.tick()
# print(a)