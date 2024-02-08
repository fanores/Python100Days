####################################
# Manipulating F-Strings
####################################
# Round a number to two decimal places
print(round(8 / 3, 2))

# Floor division -> divide the number to a whole integer
print(8 // 3)
print(type(8 // 3))

# Inline mathematical operation
score = 0
# Instead of score = score + 1
score += 2
print(score)
score -= 1
score *= 2
score /= 2
print(score)

# Using f-strings, using integer, float and string in a print command
score = 0
height = 1.8
isWinning = True
print(f"Your score is: {score}, your height is {height}, are you winning: {isWinning}")

####################################
# Exercise math operations
####################################
print("Enter your age: \n")
age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
maxWeeks = 90 * 52
usedWeeks = int(age) * 52
availableWeeks = maxWeeks - usedWeeks

print(f"You have {availableWeeks} weeks left.")
