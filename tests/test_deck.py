from deck import Deck
from card import Card


def test_deck():
    deck = Deck()
    actual_len = len(deck.cards)
    expected_len = 52
    assert actual_len == expected_len
    assert all([isinstance(card, Card) for card in deck.cards])
