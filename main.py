import random
from art import logo
from os import system

def deal_cards():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  chosen_card = random.choice(cards)
  return chosen_card

def calculate_score(list_of_cards):
  """Take a list of cards and return the score calculated from the cards"""


  if len(list_of_cards) == 2 and sum(list_of_cards) == 21:
    return 0
    
  if 11 in list_of_cards and sum(list_of_cards) > 21:
    list_of_cards.remove(11)
    list_of_cards.append(1)

  return sum(list_of_cards)

def compare_score(user_score, computer_score):
    """Compares the user's score to the computer's score and returns a string"""
    if user_score > 21 and computer_score > 21:
      return "You went over. You lose 😤"
  
    elif user_score == 0:
      return "Win with a Blackjack 😎"
      
    elif computer_score == 0:
      return "Dealer gotta a blackjack!! you lose😱"

    elif computer_score > 21:
      return "Dealer busted!! you win.😁"
      
    elif user_score > 21:
      return "You went over! you lose!😤"
    elif user_score > computer_score:
      return "\nYou win! 😃"
    elif computer_score > user_score:
      return "\nYou lose 😤"
    else:
      return "\nIt's a tie!"
    
def play_game():


  print(logo)

  player_cards = []
  dealer_cards = []
  is_game_over = False


  for number in range(2):
    player_cards.append(deal_cards())
    dealer_cards.append(deal_cards()) 

  while not is_game_over:
    player_score = calculate_score(player_cards)
    dealer_score = calculate_score(dealer_cards)

    print(f"  Your cards: {player_cards}. Your score is {player_score}")
    print(f"  Computer's first card: {dealer_cards [0]}")

    if player_score == 0 or dealer_score == 0 or player_score > 21:
      is_game_over = True

    else:    
      draw_user_a_cart = input("Type 'y' to get another card, type 'n' to pass: ")
      if draw_user_a_cart == "y":
        player_cards.append(deal_cards())
      else: 
        is_game_over = True
    
  
  while dealer_score < 17 and dealer_score != 0:
    dealer_cards.append(deal_cards())
    dealer_score = calculate_score(dealer_cards)
    

  print(f"  Your final hand: {player_cards}. Your score is {player_score}")

  if dealer_score != 0:
    print(f"  Computer's final hand: {dealer_cards}. Computer's score is {dealer_score}")
    

  print(compare_score(player_score, dealer_score))

while input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
  system('cls')
  play_game()