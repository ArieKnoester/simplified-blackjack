
import os
from table import Table


def clear_screen():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')


# Main game loop.
while True:
    user_plays = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower().strip()
    if user_plays == 'y':
        clear_screen()
        table = Table()
        table.play_blackjack()
    else:
        break
