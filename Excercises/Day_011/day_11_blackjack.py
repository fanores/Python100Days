##################################################
# Python Exercise - Blackjack Game
##################################################
"""
############## Our Blackjack House Rules #####################
# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

#################### Hints #####################
# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

# Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Then try to create your own flowchart for the program.

# Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

# Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
# user_cards = []
# computer_cards = []

# Hint 6: Create a function called calculate_score() that takes a List of cards as input
# and returns the score.
# Look up the sum() function to help you do this.

# Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

# Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

# Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

# Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

# Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

# Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

# Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
"""

# Import libraries
from day_11_blackjack_logo import blackjack_logo
import random
import os

# Blackjack functionality
def clear_screen():
    """Clears the console by running system clear command."""
    os.system('cls' if os.name == 'nt' else 'clear')

def deal_card():
    """Returns a random card from the deck."""
    # Deck of cards
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def deal_cards(deck, number_of_cards):
    """Deals a specified number of cards to the given deck and appends it to assigned deck."""
    for _ in range(number_of_cards):
        deck.append(deal_card())

def calculate_score(deck):
    """Calculates the score of the chosen deck."""
    sum_of_cards = sum(deck)
    
    # Check for blackjack (a hand with only 2 cards: ace + 10)
    if sum_of_cards == 21 and len(deck) == 2:
        return 0
    
    # Check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1.
    if 11 in deck and sum(deck) > 21:
        deck.remove(11)
        deck.append(1)

    return sum(deck)

def result_of_game(user_score, computer_score):
    """Determines and returns the result of the game based on the user and computer scores."""
    if user_score == computer_score:
        return "It's a draw 🙃"
    elif computer_score == 0:
        return "You lose, dealer has Blackjack 😱"
    elif user_score == 0:
        return "You win with a Blackjack 😎"
    elif user_score > 21:
        return "You lose, you went over. 😭"
    elif computer_score > 21:
        return "You win, opponent went over. 😁"
    elif user_score > computer_score:
        return "You win, you have higher score. 😃"
    else:
        return "You lose, dealer has higher score. 😢"

def play_blackjack():
    """Play a game of blackjack."""
    print(blackjack_logo)
    user_score = -1
    computer_score = -1
    user_cards = []
    computer_cards = []

    deal_cards(user_cards, 2)
    deal_cards(computer_cards, 2)

    # User is playing until they decide to pass or they go over 21 or get a blackjack
    is_user_playing = True
    while is_user_playing:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, your score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        # If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
        # Otherwise user needs to decide whether another card is needed or not.
        if user_score == 21 or computer_score == 21 or user_score > 21:
            is_user_playing = False
        else:
            is_user_requesting_card = input("Type 'yes' to get another card, type 'no' to pass: ")
            if is_user_requesting_card == "yes":
                deal_cards(user_cards, 1)
            else:
                is_user_playing = False
    
    # Dealer is playing until it reaches a score of at least 17 or it gets a blackjack
    while computer_score < 17 and computer_score != 0:
        deal_cards(computer_cards, 1)
        computer_score = calculate_score(computer_cards)
    
    print("-------------- Final Results -----------")
    print(f"Your cards: {user_cards}, your score: {user_score}")
    print(f"Computer's cards: {computer_cards}, computer's score: {computer_score}")
    print(result_of_game(user_score, computer_score))

# Black Jack Game
is_game_active = True
while is_game_active:
    user_wants_to_play = input("Do you want to play a game of Blackjack? Type 'yes' or 'no': ")
    clear_screen()
    if user_wants_to_play == "yes":
        play_blackjack()
    else:
        is_game_active = False
