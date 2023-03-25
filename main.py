############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from art import logo


def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  chosen_card = random.choice(cards)
  return chosen_card


def calculate_score(all_cards):
  """Take a list of cards and return the score calculated from the cards"""
  
  score = sum(all_cards)
  print(f"First - Score is: {score}")
  print(f"First - sum(all_cards) is: {sum(all_cards)}")

  if len(all_cards) == 2 and sum(all_cards) == 21:
    return 0
  if 11 in all_cards and sum(all_cards) > 21:
    for i,card in enumerate(all_cards):
      if card == 11:
        all_cards[i] = 1
    print(f"Last - Score is: {score}")
    print(f"Last - sum(all_cards) is: {sum(all_cards)}")  
    return sum(all_cards)
  return sum(all_cards)
  

def compare(user_score, computer_score):
  
  if user_score > 21 and computer_score > 21:
    return "You went over. You loose. 😭"
  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "You lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "You win with a Blackjack! 😎"
  elif user_score > 21:
    return "You went over. You loose. 😭"
  elif computer_score > 21:
    return "Opponent went over. You win! 😁😃"
  elif user_score > computer_score:  
    return "You win! 😃"
  else:
    return "You lose 😤"


def game_on():
  
  print(logo)
  
  user_cards = []
  computer_cards = []

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  keep_playing = True
  while keep_playing == True:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print("=============================================================================")
    print(f"\n      Your first cards : {user_cards}, current score: {user_score}")
    print(f"      Computer's card: [{computer_cards[0]}]")
    print("=============================================================================")    
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
      print(user_score)
      keep_playing = False
    else:
        while True: 
          more_cards = input("\nType 'y' to get another card, type 'n' to pass: ").lower()
          if more_cards == 'y':
            user_cards.append(deal_card())
            break
          elif more_cards == 'n':
            keep_playing = False
            break
          else:
            print("\n===========================")
            print("Incorrect input. Try again.")
            print("===========================")

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards) 
  print("-----------------------------------------------------------------------------")
  print(f"\n        Your final hand: {user_cards}, final score: {user_score}")
  print(f"  Computer's final hand: {computer_cards}, final score: {computer_score}\n")
  print("───────────────────────────────────")
  print(compare(user_score, computer_score))
  print("-----------------------------------------------------------------------------")


blackjack = True
while blackjack == True:
  while True:
    game = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if game == 'y':
      game_on()
      break
    elif game == 'n':
      print("\nGoodbye!")
      blackjack = False
      break
    else:
        print("\n===========================")
        print("Incorrect input. Try again.")
        print("===========================")      