##################################################
# Python - Prime Number Checker Exercise
##################################################
"""
Prime numbers are numbers that can only be cleanly divided by themselves and 1.
You need to write a function called is_prime() that checks whether if the number passed into it is a prime number or not.  It should return True or False.
NOTE: 2 is a prime number because it's only divisible by 1 and itself, but 1 is not a prime number because it is only divisible by 1.
"""

def is_prime(number):
    """Checks if the given number is a prime number."""
    if number <= 1:
        return False
    else:
        for iterrator in range(2, number):
            if number % iterrator == 0:
                return False
        return True

# Check if it is a prime number
input_number = int(input("What number do you want to check if it's a prime number?: "))
print(f"Is {input_number} a prime number?: {is_prime(input_number)}.")