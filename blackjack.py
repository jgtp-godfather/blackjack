############### Blackjack Project #####################
import random

from logo import logo

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

def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
     return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card


def compare(user_score, computer_score):

        if user_score > 21 and computer_score > 21:
            return "You went over. You lose 😤"


        if user_score == computer_score:
            return "Draw 🙃"
        elif computer_score == 0:
            return "Lose, opponent has Blackjack 😱"
        elif user_score == 0:
            return "Win with a Blackjack 😎"
        elif user_score > 21:
            return "You went over. You lose 😭"
        elif computer_score > 21:
            return "Opponent went over. You win 😁"
        elif user_score > computer_score:
            return "You win 😃"
        else:
            return "You lose 😤"
def play_game():
    user_cards = []
    computer_cards = []
    for _ in range(2):
      user_cards.append(deal_cards())
      computer_cards.append(deal_cards())
    is_game_over=False
    while is_game_over==False:
      user_score=calculate_score(user_cards)
      computer_score=calculate_score(computer_cards)
      print(f"   Your score is {user_score}. Your cards are {user_cards}.")
      print(f"  Computer has {computer_cards[0]}.")
      if user_score==0 or computer_score==0 or user_score > 21:
        is_game_over=True
      else:
        option=input("Do you want another card? Press 'y or 'n'.")
        if option=='y':
          user_cards.append(deal_cards())
        elif option=='n':
          is_game_over=True
      
      
    while computer_score!=0 and computer_score<17:
      computer_cards.append(deal_cards())
      computer_score=calculate_score(computer_cards)
    
    print (f"  Your final hand is {user_cards}. Computer's final hand is {computer_cards} ")
    print(compare(user_score, computer_score)) 

another_game=input("Do you want to start game?")
while another_game=='y':
  print(logo)
  play_game()
  another_game=input("Do you want to start another game?")   