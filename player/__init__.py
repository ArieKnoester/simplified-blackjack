from blackjack_score import score_hand

class Player:
    def __init__(self, *, table):
        self.cards = []
        self.table = table

    def take_card(self, card):
        self.cards.append(card)

    @property
    def score(self):
        return score_hand(self.cards)
    
    @property
    def bust(self) -> bool:
        return self.score > 21

    @property
    def blackjack(self):
        """Checks for blackjack which can only occur with an ace and a 10 card"""
        return self.score == 21 and len(self.cards) == 2

    def take_turn(self):
        while True:
            self.display_turn()
            takes_card = (
                input("Type 'y' to get another card, type 'n' to pass: ")
                .lower()
                .strip()
            )
            if takes_card == "y":
                self.take_card(self.table.deck.deal_card())
                if self.bust:
                    break
            else:
                break

    def display_turn(self):
        dealers_first_card = self.table.dealer.cards[0]
        print(f"\tYour cards: {self.cards}, current score {self.score}")
        print(f"\tDealer's first card: {dealers_first_card}")
