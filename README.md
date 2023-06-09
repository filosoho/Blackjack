# Blackjack
This is a simple command-line Blackjack game that you can play with the computer acting as the dealer. The game follows the basic rules of Blackjack, with a few customizations.

# Game Rules

* The deck is unlimited in size.
* There are no jokers.
* The Jack/Queen/King all count as 10.
* The Ace can count as 11 or 1.
* Use the following list as the deck of cards: cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10].
* The cards in the list have equal probability of being drawn.
* Cards are not removed from the deck as they are drawn.
* The computer is the dealer.

# Getting Started
To run the game, simply run:  
~~~
main.py
~~~
The game will prompt you to input whether you want to play or not.

# Gameplay
* You will start with two cards, and the dealer (computer) will start with one card.  
* You can choose to hit (draw another card) or stand (keep your current hand) to get as close to 21 as possible without going over.  
* Once you stand, the dealer will draw cards until they have 17 or more points.  
* If you win, you get double your bet. If you lose, you lose your bet. If you tie, you keep your bet.   

~~~
#################### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

.------.            _     _            _    _            _
|A_  _ |.          | |   | |          | |  (_)          | |
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |
      `------'                           |__/

Do you want to play a game of Blackjack? Type 'y' or 'n': y

=============================================================================

      Your first cards : [5, 3], current score: 8
      Computer's card: [10]
=============================================================================

Type 'y' to get another card, type 'n' to pass: y

=============================================================================

      Your first cards : [5, 3, 11], current score: 19
      Computer's card: [10]
=============================================================================

Type 'y' to get another card, type 'n' to pass: n

-----------------------------------------------------------------------------

        Your final hand: [5, 3, 11], final score: 19
  Computer's final hand: [10, 3, 3, 8], final score: 24

───────────────────────────────────
Opponent went over. You win! 😁😃
-----------------------------------------------------------------------------

Do you want to play a game of Blackjack? Type 'y' or 'n': 
~~~  

# Contributing
If you would like to contribute to this program, feel free to submit a pull request. Please include a detailed description of the changes made and the reasons for the changes.

# License
Feel free to use and modify the code as per your requirements.
