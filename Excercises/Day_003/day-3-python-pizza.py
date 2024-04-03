####################################
# Python Pizza Excercise
####################################

print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size S, M, L do you want? ") # What size pizza do you want? S, M, or L
add_pepperoni = input("Pepperoni, Y or N? ") # Do you want pepperoni? Y or N
extra_cheese = input("Extra cheese, Y or N? ") # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

pizza_price = 0

# Price based on size
if size == "S":
    pizza_price = 15
elif size == "M":
    pizza_price = 20
elif size == "L":
    pizza_price = 25
else:
    pizza_price = 1000000

# Extra #1 - pepperoni
if add_pepperoni == "Y":
    if size == "S":
        pizza_price += 2
    elif size == "M":
        pizza_price += 3
    elif size == "L":
        pizza_price += 3
    else:
        pizza_price += 1000000
# Extra #2 - cheese
if extra_cheese == "Y":
    pizza_price += 1

print(f"Your final bill is: ${pizza_price}.")