
import os
from art import logo
from player import Player


def clear_screen():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')


def display_turn(player, dealers_first_card):
    print(f"\tYour cards: {player.cards}, current score {player.score}")
    print(f"\tDealer's first card: {dealers_first_card}")


def display_final_turn(player, dealer):
    print(f"\tYour final hand: {player.cards}, final score: {player.score}")
    if not player.bust:
        print(f"\tDealer's final hand: {dealer.cards}, final score: {dealer.score}")


def player_turn(player, dealers_first_card):
    player_takes_card = True
    while player_takes_card:
        display_turn(player, dealers_first_card)
        takes_card = input("Type 'y' to get another card, type 'n' to pass: ").lower().strip()
        if takes_card == 'y':
            player.draw_card()
            if player.bust:
                player_takes_card = False
        elif takes_card != 'y':
            player_takes_card = False


def dealer_turn(player, dealer):
    while (
            dealer.score < 17
            or
            dealer.score < player.score
    ):
        dealer.draw_card()


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
    dealer = Player()
    print(logo)

    # if there is a blackjack immediately show who won.
    if player.blackjack or dealer.blackjack:
        display_final_turn(player, dealer)
        display_winner(player, dealer)
        return

    # If no blackjack, player takes their turn
    player_turn(player, dealers_first_card=dealer.cards[0])

    # If player busts immediately display the winner.
    if player.bust:
        display_final_turn(player, dealer)
        display_winner(player, dealer)
        return

    # If player didn't bust, dealer takes its turn.
    dealer_turn(player, dealer)

    # Evaluate game and display the winner.
    display_final_turn(player, dealer)
    display_winner(player, dealer)


# Main game loop.
play_game = True
while play_game:
    user_plays = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower().strip()
    if user_plays == 'y':
        clear_screen()
        play_blackjack()
    else:
        play_game = False
