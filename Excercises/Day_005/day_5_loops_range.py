#########################################
# Python Loops - For Loops & Range
#########################################

# FOR LOOP & Range
# for number in range(a, b):
#   do something, e.g. print(number)

# For Loop within a specified range
print("Print a range 1 to 10 (not included): ")
for number in range(1, 10):
    print(number)

# For Loop within a specified range with a step specified (i.e. increased by what?)
print("Print a range 1 to 10 (included), with 2 as a step increment: ")
for number in range(1, 11, 2):
    print(number)

# The Gauss Challenge -> total of numbers 1..100, inclusive 1 and 100
print("The Gauss Challenge: ")
total_numbers_sum = 0
for number in range(1, 101):
    total_numbers_sum += number

print(f"The result of Gauss Challenge is: {total_numbers_sum}")
