CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


class Player:
    def __init__(self):
        self.cards = []
        self.score = 0
        self.blackjack = False
        self.busted = False
