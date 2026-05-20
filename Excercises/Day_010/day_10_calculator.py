##################################################
# Python Functions - Calculator Exercise
##################################################

# Import gavel logo
from day_10_calculator_art import calculator_logo

# Calculator operations
def add(number_1, number_2):
    return number_1 + number_2

def subtract(number_1, number_2):
    return number_1 - number_2

def multiply(number_1, number_2):
    return number_1 * number_2

def divide(number_1, number_2):
    return number_1 / number_2

calculator_operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# Calculator logic
def calculator_start():
    # Start calculator user interface
    print(calculator_logo)

    # Initialize & Start calculator operations loop
    is_calculator_active = True
    is_new_calculation = True

    while is_calculator_active:
        if is_new_calculation:
            number_1 = float(input("What's the first number?: "))
        
        for operation_symbol in calculator_operations:
            print(operation_symbol)
        selected_operation = input("Choose your operation: ")

        number_2 = float(input("What's the second number?: "))

        result = calculator_operations[selected_operation](number_1=number_1, number_2=number_2)
        print(f"{number_1} {selected_operation} {number_2} = {result}")

        user_decision = input(f"Type 'yes' to continue calculating with {result}, type 'no' to start a new calculation or type 'quit' to exit.\n").lower()

        if user_decision == "yes":
            is_new_calculation = False
            number_1 = result
        elif user_decision == "no":
            is_new_calculation = True
            print("Starting a new calculation...")
        else:
            is_calculator_active = False

# Start calculator
calculator_start()
