from card import all_cards
import random


class Deck:

    def __init__(self):
        self.cards = all_cards()

    def __repr__(self) -> str:
        return f"<Deck size={len(self.cards)}>"

    def shuffle(self):
        random.shuffle(self.cards)
