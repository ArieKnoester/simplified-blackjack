from card import Card, all_cards


# TODO Add tests: Each suit has 13 cards. Each color has 26 cards.
def test_all_cards():
    cards = all_cards()
    actual_len = len(cards)
    expected_len = 52
    assert actual_len == expected_len
    assert all([isinstance(card, Card) for card in cards])
