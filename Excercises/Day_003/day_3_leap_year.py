####################################
# Leap Year Determinator
####################################

# Which year do you want to check?
year = int(input("Type year: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("Leap")
        else:
            print("Not Leap")
    else:
        print("Leap")
else:
    print("Not Leap")
