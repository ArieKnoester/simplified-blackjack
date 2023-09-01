import random

CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


class Player:

    def __init__(self):
        self.cards = []
        self.score = 0
        self.blackjack = False
        self.bust = False
        for i in range(2):
            self.draw_card()
        self.set_score()
        self.check_for_blackjack()

    def draw_card(self):
        self.cards.append(random.choice(CARDS))

    def set_score(self):
        self.score = sum(self.cards)
        if self.score > 21 and 11 in self.cards:
            ace_index = self.cards.index(11)
            self.cards[ace_index] = 1
            self.set_score()
        elif self.score > 21:
            self.bust = True

    def check_for_blackjack(self):
        if self.score == 21:
            self.blackjack = True
