# simplified-blackjack

This program was created as part of a Python course. This version
of blackjack is considered simplified, because it does not take 
into account probability and does not use multiple decks. 

The original version of this program simply used 2 lists to keep 
track of the Dealer's and Player's cards. Having completed that 
requirement I refactored this to use 2 dictionaries just see if I 
could. While I was able to get all functionality working, I was 
not happy with how the code turned out. I felt it lacked readability, 
and it wasn't clear how it worked (See 'Initial commit'). This is a third attempt in which I 
wanted to try an OOP approach.

### Blackjack House Rules as defined by the course

- The deck is unlimited in size. 
- There are no jokers. 
- The Jack/Queen/King all count as 10.
- The Ace can count as 11 or 1.
- Use the following list as the deck of cards:

    `cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]`

- The cards in the list have equal probability of being drawn.
- Cards are not removed from the deck as they are drawn.
- The computer is the dealer. 
- The dealer must draw if the total value of its cards is less than 17.