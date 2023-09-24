from dataclasses import dataclass
from enum import Enum
from itertools import product


class CardSuit(Enum):
    SPADES = "spades"
    HEARTS = "hearts"
    DIAMONDS = "diamonds"
    CLUBS = "clubs"


class CardRank(Enum):
    ACE = "ace"
    TWO = "two"
    THREE = "three"
    FOUR = "four"
    FIVE = "five"
    SIX = "six"
    SEVEN = "seven"
    EIGHT = "eight"
    NINE = "nine"
    TEN = "ten"
    JACK = "jack"
    QUEEN = "queen"
    KING = "king"


class CardColor(Enum):
    RED = "red"
    BLACK = "black"


@dataclass
class Card:
    suit: CardSuit
    rank: CardRank

    @property
    def color(self) -> CardColor:
        if self.suit in [CardSuit.HEARTS, CardSuit.DIAMONDS]:
            return CardColor.RED
        elif self.suit in [CardSuit.CLUBS, CardSuit.SPADES]:
            return CardColor.BLACK


def all_cards() -> list[Card]:
    return list(
        Card(suit=suit, rank=rank)
        for rank, suit in product(CardRank, CardSuit)
    )

# card = Card(suit=CardSuit.CLUBS, rank=CardRank.THREE)
