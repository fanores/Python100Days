##########################################
# Python Project - Hangman Game
##########################################

# What is a Hangman Game?
# Go to Wikipedia: https://en.wikipedia.org/wiki/Hangman_(game)
# Or give it a try here: https://hangmanwordgame.com/

# Step 1: Choose a word from a list of words
# Step 2: Ask the user to guess a letter
# Step 3: Check if the letter is in the word
# Step 4: If the letter is in the word, reveal its position(s)
# Step 5: If the letter is not in the word, decrease the number of attempts
# Step 6: Repeat steps 2-5 until the user guesses the word or runs out of attempts
# Step 7: Congratulate the user if they win, or reveal the word if they lose

# Import the random module to choose a random word
import random

word_list = ["ardvark", "baboon", "camel"]

random_word = random.choice(word_list)
word_length = len(random_word)
print(f'Pssst, the solution is {random_word} of length {word_length}.')

guessed_letter = input("Guess a letter: ").lower()

for letter in random_word:
    if letter == guessed_letter:
        print("True")
    else:
        print("False")

