####################################
# Python Nested Lists
####################################

# Snippet USA States
usa_states = ["Texas", "Kentucky", "Minnesota", "New York", "Alaska"]

# Print length of the list
number_of_states = len(usa_states)
print(number_of_states)

# Print item from the list
print(usa_states[number_of_states - 1])

# Nested lists
fruits = ["strawberries", "nectarines", "apples", "grapes", "cherries"]
vegetables = ["spinach", "kale", "tomatoes", "potatoes"]

mix_fruits_vegetables = [fruits, vegetables]

print(mix_fruits_vegetables)
# Print 2nd item from the first nested list => nectarines
print(mix_fruits_vegetables[0][1])
