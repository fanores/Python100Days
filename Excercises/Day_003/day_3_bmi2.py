####################################
# BMI Calculator v2.0
####################################

# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
my_bmi = weight / (height ** 2)

if my_bmi < 18.5:
    print(f"My BMI is {my_bmi}, I'm underweight.")
elif my_bmi < 25:
    print(f"My BMI is {my_bmi}, I'm of normal weight.")
elif my_bmi < 30:
    print(f"My BMI is {my_bmi}, I'm of slightly overweight.")
elif my_bmi < 35:
    print(f"My BMI is {my_bmi}, I'm obese.")
else:
    print(f"My BMI is {my_bmi}, I'm clinically obese.")
