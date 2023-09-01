
import random
import os
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def clear_screen():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')


def draw_card():
    return random.choice(cards)


def set_score(participants, participant):
    if participant == "all":
        participants["player"]["score"] = sum(participants["player"]["cards"])
        participants["dealer"]["score"] = sum(participants["dealer"]["cards"])
    else:
        participants[participant]["score"] = sum(participants[participant]["cards"])


def display_turn(participants):
    print(f"\tYour cards: {participants['player']['cards']}, current score {participants['player']['score']}")
    print(f"\tDealer's first card: {participants['dealer']['cards'][0]}")


def display_final_turn(participants, player_busted):
    print(f"\tYour final hand: {participants['player']['cards']}, final score: {participants['player']['score']}")
    if not player_busted:
        print(
            f"\tDealer's final hand: {participants['dealer']['cards']}, final score: {participants['dealer']['score']}")


def check_for_blackjack(participants):
    has_blackjack = False
    for participant in participants.values():
        if participant["score"] == 21:
            participant["blackjack"] = True
            has_blackjack = True
    return has_blackjack


def replace_ace_with_one(participants, participant):
    position = participants[participant]["cards"].index(11)
    participants[participant]["cards"][position] = 1


def check_for_bust(participants, participant):
    if participants[participant]["score"] > 21:
        participants[participant]["busted"] = True


def player_turn(participants):
    player_takes_card = True
    while player_takes_card:
        display_turn(participants)
        takes_card = input("Type 'y' to get another card, type 'n' to pass: ").lower().strip()
        if takes_card == 'y':
            participants["player"]["cards"].append(draw_card())
            set_score(participants, participant="player")
            if participants["player"]["score"] > 21 and 11 in participants["player"]["cards"]:
                replace_ace_with_one(participants, participant="player")
                set_score(participants, participant="player")
            elif participants["player"]["score"] > 21:
                player_takes_card = False
        elif takes_card != 'y':
            player_takes_card = False


def dealer_turn(participants):
    while (
            participants["dealer"]["score"] < 17
            or
            participants["dealer"]["score"] < participants["player"]["score"]
    ):
        participants["dealer"]["cards"].append(draw_card())
        set_score(participants, participant="dealer")


def display_winner(participants):
    player_blackjack = participants["player"]["blackjack"]
    dealer_blackjack = participants["dealer"]["blackjack"]
    player_score = participants["player"]["score"]
    dealer_score = participants["dealer"]["score"]
    player_busted = participants["player"]["busted"]
    dealer_busted = participants["dealer"]["busted"]

    if player_blackjack and not dealer_blackjack:
        print("You win with Blackjack 😎")
    elif dealer_blackjack and not player_blackjack:
        print("Dealer wins with Blackjack 😎")
    elif player_score == dealer_score:
        print("Draw 🙃")
    elif player_busted:
        print("You went over. You lose 😭")
    elif dealer_busted:
        print("Dealer went over. You win 😁")
    elif dealer_score > player_score:
        print("You lose 😤")


def play_blackjack():
    # (Re)initialize Dictionary.
    participants = {
        "player": {
            "cards": [],
            "score": 0,
            "blackjack": False,
            "busted": False
        },
        "dealer": {
            "cards": [],
            "score": 0,
            "blackjack": False,
            "busted": False
        }
    }
    print(logo)

    # Get the first round of cards.
    for i in range(2):
        participants["player"]["cards"].append(draw_card())
        participants["dealer"]["cards"].append(draw_card())
    # print(participants)

    # set card value totals for player and dealer
    set_score(participants, participant="all")
    # print(participants)

    # Bug Fix: Quick fix in case 2 aces were drawn by the player
    # or dealer on the first turn. This really should be fixed in the
    # set_score function instead.
    if participants["player"]["score"] > 21 and 11 in participants["player"]["cards"]:
        replace_ace_with_one(participants, participant="player")
        set_score(participants, participant="player")
    elif participants["player"]["score"] > 21 and 11 in participants["dealer"]["cards"]:
        replace_ace_with_one(participants, participant="dealer")
        set_score(participants, participant="dealer")

    # Check for a blackjack
    blackjack = check_for_blackjack(participants)

    # if there is a blackjack immediately show who won.
    if blackjack:
        display_final_turn(participants, player_busted=False)
        display_winner(participants)
        return

    # If no blackjack, player takes their turn
    player_turn(participants)

    # Check if the player went over 21.
    # If player busts immediately display the winner.
    check_for_bust(participants, participant="player")
    player_busted = participants["player"]["busted"]
    if player_busted:
        display_final_turn(participants, player_busted=True)
        display_winner(participants)
        return

    # If player didn't bust, dealer takes its turn.
    dealer_turn(participants)
    # print(participants)

    # Check if dealer busted.
    check_for_bust(participants, participant="dealer")
    # print(participants)

    # Evalute game and display the winner.
    display_final_turn(participants, player_busted)
    display_winner(participants)


# Main game loop.
play_game = True
while play_game:
    user_plays = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower().strip()
    if user_plays == 'y':
        clear_screen()
        play_blackjack()
    else:
        play_game = False
