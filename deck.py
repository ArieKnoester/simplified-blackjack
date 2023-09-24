from card import Card, all_cards
import random


class Deck:
    """A face down deck of cards:
    The Card in the first position (0) is the bottom Card.
    The Card in the last position (-1) is the top Card."""
    def __init__(self):
        self.cards = all_cards()

    def __repr__(self) -> str:
        return f"<Deck size={len(self.cards)}>"

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self) -> Card:
        return self.cards.pop()
