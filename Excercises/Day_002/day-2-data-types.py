####################################
# Exercise data types
####################################

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
# Write your code below this line 👇
number_1 = int(two_digit_number[0])
number_2 = int(two_digit_number[1])
sum = number_1 + number_2
print(sum)

####################################
# Check for variable type and convert number to string
number_of_characters = len(input("What is your name? "))

print(type(number_of_characters))

# Print and convert to string
print("Your name has " + str(number_of_characters) + " characters.\n")

# Convert number to float
number_conv_to_float = float(123)
print(type(number_conv_to_float))

# Printing input converted as number and converted as string
print(70 + float("100.7"))
print(str(70) + str(100))
