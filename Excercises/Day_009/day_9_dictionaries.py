##################################################
# Python Dictionaries
# A dictionary is a collection which is unordered, 
# changeable and indexed. In Python dictionaries 
# are written with curly brackets, and they have 
# keys and values.
##################################################

# Working with dictionaries
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# Retrieving items from a dictionary
print(programming_dictionary["Bug"])

# Adding new items to a dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

# Editing existing items in a dictionary
# If the key already exists, the value will be updated, if not, a new key-value pair
# will be added to the dictionary.
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary["Bug"])

# Looping through a dictionary
for key in programming_dictionary:
    print(key)  # Prints the keys of the dictionary
    print(programming_dictionary[key])  # Prints the value of the key from the dictionary

# Clear existing dictionary
programming_dictionary = {}
print(programming_dictionary)
