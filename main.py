import random
from os import system

def deal_cards():
  """Deals 2 random cards"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  chosen_card = random.choice(cards)
  return chosen_card

def calculate_score(list_of_cards):


  if len(list_of_cards) == 2 and sum(list_of_cards) == 21:
    return 0
    
  if 11 in list_of_cards and sum(list_of_cards) > 21:
    list_of_cards.remove(11)
    list_of_cards.append(1)
    return sum(list_of_cards)
  else:
    return sum(list_of_cards)


want_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
player_score = 0
dealer_score = 0
player_cards = []
dealer_cards = []
while want_to_play == "y":


  for number in range(2):
    player_cards.append(deal_cards())
    dealer_cards.append(deal_cards()) 

  player_score = calculate_score(player_cards)
  dealer_score = calculate_score(dealer_cards)

  if dealer_score < 17:
    dealer_cards.append(deal_cards())
    dealer_score = calculate_score(dealer_score)

  if player_score == 0:
    print("You gotta a blackjack!! you wins")
    print(f"  Your cards: {player_cards}, your score is 21")
    
  elif dealer_score == 0:
    print("Dealer gotta a blackjack!! you lose")
    print(f"  Your cards: {player_cards}, your score is {player_score}")
    print(f"  Dealer's cards: {dealer_cards}, dealer's score is 21")

  if dealer_score > 21:
    print("Dealer busts. You win!")
    print(f"  Your final hand: {player_cards}. Your score is {player_score}")
    print(f"  Computer's final hand: {dealer_cards}. Computer's score is {dealer_score}")
    
  else:
    print(f"  Your cards {player_cards}. Your score is {player_score}.")
    print(f"  Computer's first card: {dealer_cards [0]}")


  while input("Type 'y' to get another card, type 'n' to pass: ").lower() == "y":
    player_cards.append(deal_cards())
    player_score = calculate_score(player_cards)
    if player_score > 21:
      print("You went over! Computer wins!")

    print(f"  Your cards: {player_cards}. Your score is {player_score}")
    print(f"  Computer's first card: {dealer_cards [0]}")

  print(f"  Your final hand: {player_cards}. Your score is {player_score}")
  print(f"  Computer's final hand: {dealer_cards}. Computer's score is {dealer_score}")

  if player_score > dealer_score:
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
    
