# File Name: counter.py
# Author: AMITTAI JOEL SIAVAVA WEKESA
# Date: 14th October, 2020
# Purpose: SA 7 -- Card class

# Creating the Card class:
class Card:

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        if self.value == 13:
            self.value_in_words = "King"
        elif self.value == 12:
            self.value_in_words = "Queen"
        elif self.value == 11:
            self.value_in_words = "Jack"
        else:
            self.value_in_words = str(self.value)

        if self.suit == 1:
            self.suit_in_words = "clubs"
        elif self.suit == 2:
            self.suit_in_words = "spades"
        elif self.suit == 3:
            self.suit_in_words = "diamonds"
        elif self.suit == 4:
            self.suit_in_words = "hearts"

        self.name = self.value_in_words + " of " + self.suit_in_words
        return self.name



