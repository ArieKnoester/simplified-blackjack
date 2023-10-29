from art import logo
from player import Player
from player.dealer import Dealer
from deck import Deck


class Table:
    def __init__(self):
        self.player = Player(table=self)
        self.dealer = Dealer(table=self)
        self.deck = Deck().shuffle()

    def play_blackjack(self):
        self.deck.reset()
        self.deck.shuffle()
        print(logo)

        # Check the table for blackjacks.
        for current_player in (self.player, self.dealer):
            if current_player.blackjack:
                self._display_final_turn()
                return

        # If no blackjack, players take their turns
        for current_player in (self.player, self.dealer):
            current_player.take_turn()
            if current_player.bust:
                self._display_final_turn()
                return

        # Evaluate game and display the winner.
        self._display_final_turn()

    def _display_final_turn(self):
        print(
            f"\tYour final hand: {self.player.cards}, final score: {self.player.score}"
        )
        if not self.player.bust:
            print(
                f"\tDealer's final hand: {self.dealer.cards}, final score: {self.dealer.score}"
            )
        self._display_winner()

    def _display_winner(self):
        if self.player.blackjack and not self.dealer.blackjack:
            print("You win with Blackjack 😎\n")
        elif self.dealer.blackjack and not self.player.blackjack:
            print("Dealer wins with Blackjack 😎\n")
        elif self.player.score == self.dealer.score:
            print("Draw 🙃\n")
        elif self.player.bust:
            print("You went over. You lose 😭\n")
        elif self.dealer.bust:
            print("Dealer went over. You win 😁\n")
        elif self.dealer.score > self.player.score:
            print("You lose 😤\n")
