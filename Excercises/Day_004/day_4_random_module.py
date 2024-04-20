# Random Module
# For more information go to: https://askpython.com
import random
import day_4_dummyModule

# Use local python module
print(day_4_dummyModule.pi)

# Use random module to generate random numbers
random_integer = random.randint(1, 10)
print(random_integer)

# Use random module to generate random decimal 1 ~ 5
random_float = random.random() * 5
print(random_float)
