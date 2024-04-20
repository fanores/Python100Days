####################################
# Python Logical Operators
####################################

# AND operator
# if condition1 and condition2:
#   do something

# OR operator
# if condition1 or condition2:
#   do something

# NOT operator
# if not condition1:
#   do something

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
    elif (age >= 45) and (age <= 55):
        ticket_price += 0
    else:
        print("Ticket price is 20 EUR.")
        ticket_price = 20

    wants_photo = input("Do you want a drink as well? Y or N: ")
    if wants_photo == "Y":
        ticket_price += 3

    print(f"Final price for the bill is {ticket_price} EUR.")
else:
    print("Your are NOT tall enough!")