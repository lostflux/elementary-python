# File Name: timer.py
# Author: AMITTAI JOEL SIAVAVA WEKESA
# Date: 11th October, 2020
# Purpose: SA 6 -- Timer class

# imports
from counter import Counter
class Timer:

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

        self.hour_count = Counter(24, self.hours, 2)
        self.minute_count = Counter(60, self.minutes, 2)
        self.second_count = Counter(60, self.seconds, 2)

    def __str__(self):
        current_time = str(self.hour_count) + ":" + str(self.minute_count) + ":" + str(self.second_count)
        return current_time

    def tick(self):
        if self.second_count.tick():
            if self.minute_count.tick():
                self.hour_count.tick()

    def is_zero(self):
        return self.second_count == self.minute_count == self.hour_count == 0
