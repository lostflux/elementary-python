# File Name: counter.py
# Author: AMITTAI JOEL SIAVAVA WEKESA
# Date: 14th October, 2020
# Purpose: SA 7 -- Deck class

# imports:
import random

from card import Card


# Creating the Deck class:
class Deck:

    # __init__ method:
    def __init__(self, number_of_cards=52):
        self.deck = []
        self.hand = []
        self.number_of_suits = 4
        self.number_of_cards = number_of_cards
        self.card_list = []
        self.cards_per_suit = 13

    # Method to generate a deck of cards
    def add_standard_cards(self):
        for number in range(1, self.cards_per_suit + 1):
            for suit in range(1, self.number_of_suits + 1):
                card = Card(number, suit)
                self.deck.append(card)
        self.card_list = self.get_list()
        return self.deck

    # Method to shuffle deck of cards:
    def shuffle(self):
        for index in range(len(self.deck)):
            card = self.deck.pop(index)
            self.deck.insert(- random.randint(0, len(self.deck)), card)
        self.card_list = self.get_list()
        return self.deck

    # Method to deal a hand of cards
    def deal(self, cards_in_hand):
        self.hand = Deck(number_of_cards=0)
        for card in self.deck[-cards_in_hand::1]:
            self.hand.deck.append(card)
            self.deck.remove(card)
        self.hand.card_list = self.hand.get_list()
        self.card_list = self.get_list()
        # print(self.hand.get_list())
        return self.hand

    # Method to generate a string list of cards:
    def get_list(self):
        self.card_list = []
        for card in self.deck:
            self.card_list.append(card.__str__())
        return self.card_list







