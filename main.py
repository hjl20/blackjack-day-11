############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

import art
import random
from replit import clear
from time import sleep

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card(hand):
  hand.append(random.choice(cards))

def ace_to_one(hand):
  """
  Changes the first 11 (ace) in a hand to a 1 and returns the new sum of hand
  """
  ace_index = hand.index(11)
  hand[ace_index] = 1
  return sum(hand)

def show_new_card(hand):
  newest_card_index = len(hand) - 1
  if hand[newest_card_index] == 11:
    print("  Drew an ace")
  else:
    print(f"  Drew a {hand[newest_card_index]}")

def blackjack():    
  
  print(art.logo)
  print("Welcome to Blackjack!\n")

  player_hand = []
  dealer_hand = []
  player_turn = True
  dealer_turn = True
  
  for i in range(2):
    deal_card(player_hand)
  deal_card(dealer_hand)

  #Sum up hands and show cards
  player_sum = sum(player_hand)
  dealer_sum = sum(dealer_hand)
  
  print(f"  Your cards: {player_hand} = {player_sum}")
  print(f"  Dealer's has: {dealer_hand[0]}")
  print("")
  
  #Player's turn
  while player_turn:
    print("--Player's turn--\n")
    draw_card = input("Draw a card? y/n: ")
    print("")
  
    #Player chooses hit
    if draw_card == "y":
      deal_card(player_hand)
      show_new_card(player_hand)
      player_sum = sum(player_hand)
      
      #Player has ace and over 21
      if player_sum > 21 and 11 in player_hand:
        player_sum = ace_to_one(player_hand)
        
      #Player busts (no ace and over 21)
      elif player_sum > 21:
        print("\nPlayer busts. You lose!")
        
        #End all turns to end game early
        player_turn = False
        dealer_turn = False

      #Show hand after each hit
      print(f"  Your cards: {player_hand} = {player_sum}\n")
      sleep(1)
      
    #Player stands
    elif draw_card =="n":
      player_turn = False

    #Invalid input
    else:
      print("Please choose either y/n\n")
  
  #Dealer's turn and must hit while under 16 and stand at 17
  while dealer_turn:
    print("--Dealer's turn--\n")
    sleep(2)
    
    #Dealer hits while under 17
    if dealer_sum < 17:
      deal_card(dealer_hand)
      show_new_card(dealer_hand)
      dealer_sum = sum(dealer_hand)
  
      #Dealer has ace and over 21
      if dealer_sum > 21 and 11 in dealer_hand:
        dealer_sum = ace_to_one(dealer_hand)
  
      #Dealer busts (no ace and over 21)
      elif dealer_sum > 21:
        print("\nDealer busts. You win!")

        #End turn to end game early
        dealer_turn = False

      #Show dealer's hand after each hit
      print(f"  Dealer's cards: {dealer_hand} = {dealer_sum}\n")
      sleep(1)

    #Dealer stands (all turns over)
    else:
      dealer_turn = False
      print("Dealer stands..\n")
      sleep(2)

      #Compare totals to end game
      if player_sum > dealer_sum:
        print("You win!\n")
      elif dealer_sum > player_sum:
        print("You lose!\n")
      else:
        print("It's a tie!\n")

  print(f"  Your hand: {player_hand}")
  print(f"  Dealer's hand: {dealer_hand}")
  print(f"Final score: Player: {player_sum}, Dealer: {dealer_sum}")

  #Ask player if they want to replay or end program
  replay = input("\nDo you want to play again? y/n: ")
  if replay == "y":
    clear()
    blackjack()
  else:
    return

blackjack()
