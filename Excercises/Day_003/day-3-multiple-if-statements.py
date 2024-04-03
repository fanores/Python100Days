####################################
# Multiple IF statements
####################################

# IF / ELIF / ELSE
# if condition1:
#   do A
# elif condition2:
#   do B
# else:
#   do C

# MULTIPLE IF
# if condition1:
#   do A
# if condition2:
#   do B
# if condition3:
#   do C

print("Welcome to the fair!")
height = int(input("What is your height in cm? "))
ticket_price = 0

if height >= 150:
    print("Your are tall enough.")

    age = int(input("How old are you? "))
    if age < 12:
        print("Ticket price is 5 EUR.")
        ticket_price = 5
    elif age <= 18:
        print("Ticket price is 10 EUR.")
        ticket_price = 10
    else:
        print("Ticket price is 20 EUR.")
        ticket_price = 20

    wants_photo = input("Do you want a drink as well? Y or N: ")
    if wants_photo == "Y":
        ticket_price += 3

    print(f"Final price for the bill is {ticket_price} EUR.")
else:
    print("Your are NOT tall enough!")