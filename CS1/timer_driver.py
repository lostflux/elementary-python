# File Name: timer_driver.py
# Author: AMITTAI JOEL SIAVAVA WEKESA
# Date: 14th October, 2020
# Purpose: SA 6 -- Timer class driver

# Imports:
from timer import Timer
from bibek_timedr import Timer
# Creating Timer object
countdown = Timer(1, 30, 00)

# Loop to repeatedly tick the timer until "00:00:00"
# And print values to console
while True:
    print(countdown)
    if countdown.is_zero():
        break
    else:
        countdown.tick()
