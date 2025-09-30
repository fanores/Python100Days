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

# 1. Pick a random word from the word_list and assign it to a variable called random_word
random_word = random.choice(word_list)
word_length = len(random_word)

# 2. Set a variable that will display the current state of the guessed word 
display_word = ""
for character in range(word_length):
    display_word += "_"

# 3. Output the word to the console for the user to see
print(f'Pssst, the solution is {random_word} of length {word_length}.')
print(f"{display_word}")

# 4. Ask the user for a letter
is_word_guessed = False
guessed_letters = []
while not is_word_guessed:
    guessed_letter = input("Guess a letter: ").lower()
    display_word = ""
    
    # 5. Process if the letter exists in the random_word
    for letter in random_word:
        if letter == guessed_letter:
            display_word += guessed_letter
            guessed_letters.append(guessed_letter)
        elif letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"
            
    # 6. Show the result of the guessed letters
    print(display_word)

    # 7. Assess if the user has guessed all the letters
    if "_" not in display_word:
        is_word_guessed = True
