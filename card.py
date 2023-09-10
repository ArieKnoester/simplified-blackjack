from dataclasses import dataclass
from enum import Enum
from itertools import product


class CardSuit(Enum):
    SPADES = "spades"
    HEARTS = "hearts"
    DIAMONDS = "diamonds"
    CLUBS = "clubs"


class CardValue(Enum):
    ACE = "ace"
    TWO = "two"
    THREE = "three"


@dataclass
class Card:
    suit: CardSuit
    value: CardValue


def all_cards() -> list[Card]:
    return list(product(CardValue, CardSuit))
