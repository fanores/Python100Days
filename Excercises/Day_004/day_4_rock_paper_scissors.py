#######################################
# Python Rock, Paper, Scissors Game
#######################################
import random

# List of the rock, paper, scissors drawings
rock_picture = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
rock = 0

paper_picture = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
paper = 1

scissors_picture = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
scissors = 2

# 0. List of possibilities
choices = [rock_picture, paper_picture, scissors_picture]

# 1. Ask the user for his choice
print("What do you Choose? ")
user_choice = int(input("Type 0 ro ROCK, 1 for PAPER or 2 for SCISSORS" + "!\n"))

# 2. Ask the computer for his choice
computer_choice = random.randint(0, 2)

# 3. Determine the result
result = ""
if user_choice == computer_choice:
    result = "Draw"
elif user_choice == rock:
    if computer_choice == paper:
        result = "You loose!"
    else:
        result = "You win!"
elif user_choice == paper:
    if computer_choice == scissors:
        result = "You loose!"
    else:
        result = "You win!"
elif user_choice == scissors:
    if computer_choice == rock:
        result = "You loose!"
    else:
        result = "You win!"
else:
    result = "Invalid input!"

# 4. Print choices & result
if user_choice >= 3 or user_choice < 0:
    print("Result: " + result)
else:
    print("User's choice:")
    print(choices[user_choice])

    print("Computer's choice:")
    print(choices[computer_choice])

    print("Result: " + result)
