##################################################
# Python - Local & Global Scope
##################################################

# Global constants
# Convention is to use uppercase letters for global constants to differentiate them from variables.
PI = 3.14159

# Global Variables
my_variable = 1
my_other_global_variable = 3

# Functions
def my_function():
    # Local variable
    my_variable = 2
    print(f"Inside the function, my_variable is: {my_variable}")
    print(f"Inside the function, my_other_global_variable is: {my_other_global_variable}")

# Program execution
my_function()
print(f"Outside the function, my_variable is: {my_variable}")
print(f"Outside the function, my_other_global_variable is: {my_other_global_variable}")

# There is no block scope in Python, only function scope. This means that variables defined inside a function are not accessible outside of that function, but variables defined outside of a function (global variables) are accessible inside the function unless they are shadowed by a local variable with the same name.
game_level = 1

if game_level < 5:
    level_up_message = "You have leveled up!"
    
# Print content of level_up_message variable outside of the IF BLOCK to demonstrate that it is accessible due to the lack of block scope in Python.
print(level_up_message)

# Modifying global variables inside a function
def modify_global_variable():
    global my_variable  # Declare that we want to use the global variable
    my_variable = 100  # Modify the global variable

modify_global_variable()
print(f"Modified global variable, my_variable is: {my_variable}")

# Other way to modify global variables
def modify_global_variable_attempt_2(variable_to_modify):
    return variable_to_modify + 900

my_variable = modify_global_variable_attempt_2(my_variable)
print(f"Modified global variable using return statement, my_variable is: {my_variable}")

# Working with constants
def print_pi():
    print(f"The value of PI is: {PI}")

print_pi()