# Python Lists
# Example 1 of a List
fruits = ["apple", "peach"]

# Example 2 US States
usa_states = ["Texas", "Kentucky", "Minnesota", "New York", "Alaska"]

# Print 1st item in the list
print(usa_states[0])

# Print last item in the list
print(usa_states[-1])

# Change the value in the list item
print(usa_states[1])
usa_states[1] = "Colorado"
print(usa_states[1])

# Append new item to the list
print(usa_states)
usa_states.append("Last appended state")
print(usa_states)

# Extend the list by more items
usa_states.extend(["one more state", "another one"])
print(usa_states)
