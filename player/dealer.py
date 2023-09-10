from player import Player


class Dealer(Player):

    def __init__(self):
        super().__init__()

    def take_turn(self, *, player_score):
        while (
                self.score < 17
                or self.score < player_score
        ):
            self.draw_card()
