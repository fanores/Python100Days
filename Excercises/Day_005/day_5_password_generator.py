#########################################
# Python Loops - Password Generator
#########################################
import random

# Variables for password characters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Input screen - how long password does the user want
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Add character to the list based on user request
password_list = []

for character in range(0, nr_letters):
    password_list.append(random.choice(letters))

for character in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

for character in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

# Shuffle the contents of the password list
print(password_list)
random.shuffle(password_list)
print(password_list)

# Output the password
password = ""
for character in password_list:
    password += character

print(f"Your password is: {password}")
