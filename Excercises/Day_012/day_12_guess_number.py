##################################################
# Python Exercise - Guess the Number Game
##################################################
"""
Simple game, where user needs to guess a number between 1 and 100. After each guess, the program will tell the user if their guess is too high, too low or correct. The user has a limited number of attempts to guess the correct number, depending on the chosen difficulty level.
"""

# Importing necessary libraries
import random
from day_12_guess_number_logo import guess_number_logo

# Global constants
EASY_DIFFICULTY_ATTEMPTS = 10
HARD_DIFFICULTY_ATTEMPTS = 5
EASY_DIFFICULTY = "easy"
HARD_DIFFICULTY = "hard"

# Game functionality
def print_game_introduction():
    """Prints the game introduction and logo."""
    print(guess_number_logo)
    print("Welcome to Guess the Number game!")

def get_difficulty(chosen_difficulty):
    """Gets the number of attempts based on the chosen difficulty level."""
    if chosen_difficulty == EASY_DIFFICULTY:
        return EASY_DIFFICULTY_ATTEMPTS
    else:
        return HARD_DIFFICULTY_ATTEMPTS

def get_random_number():
    """Generates and returns a random number between 1 and 100."""
    return random.randint(1, 100)

def get_is_still_guessing_status(user_guess, random_number, user_attempts):
    """Determines if the user is still guessing based on their guess, the random number and remaining attempts."""
    if user_guess == random_number:
        return False
    elif user_attempts == 0:
        return False
    else:
        return True

def print_guess_evaluation(user_guess, random_number, attempts):
    """Prints feedback based on the user's guess."""
    if user_guess == random_number:
        print(f"You got it! The answer was {random_number}.")
    elif user_guess > random_number:
        print("Too high.")
    elif user_guess < random_number:
        print("Too low.")

    if attempts == 0 and user_guess != random_number:
        print(f"You've run out of attempts. The correct number was {random_number}. Game over.")
    elif attempts > 0 and user_guess != random_number:
        print("Guess again.")

# -1- Start game
print_game_introduction()

# -2- Start game sequence
print("I'm thinking of a number between 1 and 100.")
chosen_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
user_attempts = get_difficulty(chosen_difficulty)
random_number = get_random_number()

# -3- User guesses number until they win or run out of attempts
is_still_guessing = True
has_user_won = False
user_guess = -1
while is_still_guessing:
    print(f"You have {user_attempts} attempts remaining to guess the number.")
    user_attempts -= 1
    
    user_guess = int(input("Make a guess: "))
    print_guess_evaluation(user_guess, random_number, user_attempts)

    is_still_guessing = get_is_still_guessing_status(user_guess, random_number, user_attempts)
