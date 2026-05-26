##################################################
# Python - Local & Global Scope
##################################################

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