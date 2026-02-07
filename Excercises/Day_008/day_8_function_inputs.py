##################################################
# Python Functions with Inputs - Define a Function
##################################################

# Define a simple function with only 1 input
def greet(name):
    print(f"Hello, {name}!")

# Call the function with different arguments
name_of_person = input("Enter a name: ")
greet(name_of_person)

# Define a function with 2 inputs
def greet_with(name, location):
    print(f"Hello, {name}!")
    print(f"What is it like in {location}?")

name_of_person2 = input("Enter a name: ")
location_of_person2 = input("Enter a location: ")
# Call the function with positional arguments - order matters
greet_with(name_of_person2, location_of_person2)
# Call the function with keyword arguments - order does not matter
greet_with(location=location_of_person2, name=name_of_person2)

