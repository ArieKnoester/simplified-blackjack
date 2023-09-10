from card import all_cards


def test_all_cards():
    actual = len(all_cards())
    expected = 52
    assert actual == expected
