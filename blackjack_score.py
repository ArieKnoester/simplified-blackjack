from card import CardRank, Card

_blackjack_card_value = {
    CardRank.TWO: 2,
    CardRank.THREE: 3,
    CardRank.FOUR: 4,
    CardRank.FIVE: 5,
    CardRank.SIX: 6,
    CardRank.SEVEN: 7,
    CardRank.EIGHT: 8,
    CardRank.NINE: 9,
    CardRank.TEN: 10,
    CardRank.JACK: 10,
    CardRank.QUEEN: 10,
    CardRank.KING: 10,
    CardRank.ACE: 11,
}

def score_hand(hand: list[Card]) -> int:
    # scenario: k, 2, a, a, 6
    # outcome: 10, 2, 1, 1, 6 = 20
    number_of_aces = hand.count(CardRank.ACE)

    score = sum([_blackjack_card_value[card.rank] for card in hand])
    
    for _ in range(number_of_aces):
        if score > 21:
            score = score - 10

    return score