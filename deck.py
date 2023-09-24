from card import all_cards
import random


class Deck:

    def __init__(self):
        self.cards = all_cards()

    def shuffle(self):
        random.shuffle(self.cards)
