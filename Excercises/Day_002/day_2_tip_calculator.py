####################################
# Tip Calculator
####################################
print("Welcome to the tip calculator!")
billAmount = float(input("What was the total bill? $"))
tipPercent = int(input("How much tip would you like to give? 10%, 12%, or 15%? "))
people = int(input("How many people to split the bill? "))

tipAmount = billAmount * tipPercent / 100
totalBill = billAmount + tipAmount
billPerPerson = round(totalBill / people, 2)
# always format the number with 2 decimal places
billPerPersonFormatted = "{:.2f}".format(billPerPerson)
print(f"People split ${billPerPersonFormatted} between each other.")

# FAQ: How to round to 2 decimal places?

# Find the answer in the Q&A here: https://www.udemy.com/course/100-days-of-code/learn/lecture/17965132#questions/13315048
