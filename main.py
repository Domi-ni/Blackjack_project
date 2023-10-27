import random
from os import system
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

want_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
player_score = 0
dealer_score = 0
player_cards = []
dealer_cards = []
while want_to_play == "y":
  for number in range(2):
    chosen_card = random.choice(cards)
    player_cards.append(chosen_card)
    player_score += chosen_card
    
  print(f"  Your cards {player_cards}. Your score is {player_score}.")
  
  for number in range(3):
    chosen_card = random.choice(cards)
    dealer_cards.append(chosen_card)
    dealer_score += chosen_card
    
  if dealer_score < 17:
    chosen_card = random.choice(cards)
    dealer_cards.append(chosen_card)
    dealer_score += chosen_card
    
  print(f"  Computer's first card: {dealer_cards [0]}")

  while input("Type 'y' to get another card, type 'n' to pass: ").lower() == "y":
    chosen_card = random.choice(cards)
    player_cards.append(chosen_card)
    player_score += chosen_card
    
    print(f"  Your cards: {player_cards}. Your score is {player_score}")
    print(f"  Computer's first card: {dealer_cards [0]}")

  print(f"  Your final hand: {player_cards}. Your score is {player_score}")
  print(f"  Computer's final hand: {dealer_cards}. Computer's score is {dealer_score}")

  if dealer_score > 21 and player_score > 21:
    print("Both players bust. Nobody wins.")
  elif dealer_score > 21:
    print("Dealer busts. You win!")
  elif player_score > 21:
    print("You busted! Computer wins!")
  elif player_score > dealer_score:
    print("You win!")
  elif player_score < dealer_score:
    print("Computer wins!")
  else:
    print("It's a tie!")
  
  want_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
  if want_to_play == "y":
    system('cls')
    player_score = 0
    dealer_score = 0
    player_cards = []
    dealer_cards = []
    
