from card import Card
from deck import Deck


def test_deck():
    deck = Deck()
    actual_len = len(deck.cards)
    expected_len = 52
    breakpoint()
    assert actual_len == expected_len
    assert all([isinstance(card, Card) for card in deck.cards])


def test_deal_card():
    deck = Deck()
    expected_card = deck.cards[-1]
    actual_card = deck.deal_card()
    assert expected_card == actual_card
    assert expected_card is actual_card
    assert len(deck.cards) == 51
    assert deck.cards[-1] != actual_card
