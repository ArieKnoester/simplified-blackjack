import random
CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


class Player:

    def __init__(self, *, table):
        self.cards = []
        self.score = 0
        self.bust = False
        self.table = table
        for i in range(2):
            self.draw_card()

    def draw_card(self):
        self.cards.append(random.choice(CARDS))
        self.set_score()

    def set_score(self):
        self.score = sum(self.cards)
        if self.score > 21 and 11 in self.cards:
            ace_index = self.cards.index(11)
            self.cards[ace_index] = 1
            self.set_score()
        elif self.score > 21:
            self.bust = True

    @property
    def blackjack(self):
        """ Checks for blackjack which can only occur with an ace and a 10 card """
        return self.score == 21 and len(self.cards) == 2

    def take_turn(self):
        while True:
            self.display_turn()
            takes_card = input("Type 'y' to get another card, type 'n' to pass: ").lower().strip()
            if takes_card == 'y':
                self.draw_card()
                if self.bust:
                    break
            else:
                break

    def display_turn(self):
        dealers_first_card = self.table.dealer.cards[0]
        print(f"\tYour cards: {self.cards}, current score {self.score}")
        print(f"\tDealer's first card: {dealers_first_card}")
