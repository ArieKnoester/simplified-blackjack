
from player import Player
from player.dealer import Dealer
from art import logo


class Table:

    def __init__(self):
        self.player = Player()
        self.dealer = Dealer()

    def play_blackjack(self):

        print(logo)

        # if there is a blackjack immediately show who won.
        if self.player.blackjack or self.dealer.blackjack:
            self._display_final_turn()
            return

        # If no blackjack, player takes their turn
        self.player.take_turn(dealers_first_card=self.dealer.cards[0])

        # If player busts immediately display the winner.
        if self.player.bust:
            self._display_final_turn()
            return

        # If player didn't bust, dealer takes its turn.
        self.dealer.take_turn(player_score=self.player.score)

        # Evaluate game and display the winner.
        self._display_final_turn()

    def _display_final_turn(self):
        print(f"\tYour final hand: {self.player.cards}, final score: {self.player.score}")
        if not self.player.bust:
            print(f"\tDealer's final hand: {self.dealer.cards}, final score: {self.dealer.score}")
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
