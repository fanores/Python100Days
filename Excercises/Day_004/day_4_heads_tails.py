# Write your code below this line 👇
# Hint: Remember to import the random module first. 🎲
import random

# Use random module to generate random numbers
random_integer = random.randint(0, 1)

if random_integer == 0:
    print("Tails")
elif random_integer == 1:
    print("Heads")
else:
    print("Error")

