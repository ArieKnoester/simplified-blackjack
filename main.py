
import os
from art import logo
from player import Player
from player.dealer import Dealer


def clear_screen():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')


def display_final_turn(player, dealer):
    print(f"\tYour final hand: {player.cards}, final score: {player.score}")
    if not player.bust:
        print(f"\tDealer's final hand: {dealer.cards}, final score: {dealer.score}")
    display_winner(player, dealer)


def display_winner(player, dealer):
    if player.blackjack and not dealer.blackjack:
        print("You win with Blackjack 😎\n")
    elif dealer.blackjack and not player.blackjack:
        print("Dealer wins with Blackjack 😎\n")
    elif player.score == dealer.score:
        print("Draw 🙃\n")
    elif player.bust:
        print("You went over. You lose 😭\n")
    elif dealer.bust:
        print("Dealer went over. You win 😁\n")
    elif dealer.score > player.score:
        print("You lose 😤\n")


def play_blackjack():

    player = Player()
    dealer = Dealer()
    print(logo)

    # if there is a blackjack immediately show who won.
    if player.blackjack or dealer.blackjack:
        display_final_turn(player, dealer)
        return

    # If no blackjack, player takes their turn
    player.take_turn(dealers_first_card=dealer.cards[0])

    # If player busts immediately display the winner.
    if player.bust:
        display_final_turn(player, dealer)
        return

    # If player didn't bust, dealer takes its turn.
    dealer.take_turn(player_score=player.score)

    # Evaluate game and display the winner.
    display_final_turn(player, dealer)


# Main game loop.
play_game = True
while play_game:
    user_plays = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower().strip()
    if user_plays == 'y':
        clear_screen()
        play_blackjack()
    else:
        play_game = False
