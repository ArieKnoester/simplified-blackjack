from player import Player


class Dealer(Player):

    def __init__(self, *, table):
        super().__init__(table=table)

    def take_turn(self):
        while (
                self.score < 17
                or self.score < self.table.player.score
        ):
            self.draw_card()
