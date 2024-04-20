####################################
# Nested if / else
####################################

# if condition:
#   if another condition1:
#       do this
#   elif condition2:
#       do this 2
#   else:
#       do that
# else:
#   do that

print("Welcome to the fair!")
height = int(input("What is your height in cm? "))

if height >= 150:
    print("Your are tall enough.")

    age = int(input("How old are you? "))
    if age < 12:
        print("Ticket price is 5 EUR.")
    elif age <= 18:
        print("Ticket price is 10 EUR.")
    else:
        print("Ticket price is 20 EUR.")
else:
    print("Your are NOT tall enough!")
