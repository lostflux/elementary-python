# File Name: counter.py
# Author: AMITTAI JOEL SIAVAVA WEKESA
# Date: 14th October, 2020
# Purpose: SA 7 -- Deck class

# imports:
import random

from card import Card


# Creating the Deck class:
class Deck:

    def __init__(self, number_of_cards):
        self.deck = []
        self.hand = []
        self.number_of_suits = 4
        self.number_of_cards = number_of_cards

    def add_standard_cards(self):
        for i in range(1, self.number_of_suits):
            for j in range(1, self.number_of_cards + 1):
                card = Card(j, i)
                self.deck.append(card)
                return self.deck

    def shuffle(self):
        for index in range(len(self.deck)):
            card = self.deck.pop(index)
            self.deck.insert(random.randint(1, len(self.deck)), card)
            return self.deck

    def deal(self, cards_in_hand):
        self.hand = Deck(cards_in_hand)
        for card in self.deck[-cards_in_hand::1]:
            self.hand.deck.append(card)
            self.deck.remove(card)
        return self.hand

    def card_list(self):
        return self.deck







