##################################################
# Python Functions with Inputs - Life in Weeks
##################################################

def life_in_weeks(age):
    return (90 - age) * 52

# Call your function with hard coded values
age_of_person = int(input("Enter your age: "))
print(f"You have {life_in_weeks(age_of_person)} weeks left.")
