####################################
# Mathematical operation
####################################
# 3 + 5
# 7 - 4
# 3 * 2
# 6 / 3
# 2 ** 2 => two to the power of two

# output is a 'float'
print(6 / 3)

# Order of operations: PEMDAS
# Parentheses ()
# Exponents **
# Multiplication *
# Division /
# Addition +
# Subtraction -

# Output: 7
print(3 * 3 + 3 / 3 - 3)

# Output: 3
print(3 * (3 + 3) / 3 - 3)

####################################
# Exercise math operations
####################################
# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
bmi = (float(weight) / (float(height) ** 2))

print(int(bmi))
