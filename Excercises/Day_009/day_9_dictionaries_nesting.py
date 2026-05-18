##################################################
# Python Dictionaries - Nesting
##################################################
# { Key: [List], Key2: {Dictionary} }
##################################################

# Ordinary dictionary
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
}

# Nested dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Access "Lille" value from the travel_log dictionary
print(travel_log["France"][1])

# Nested list
nested_list = ["a", "b", ["c", "d"]]
print(nested_list[2][0])

# Nested dictionary enhanced
travel_log = {
    "France": {
        "total_visits": 12,
        "cities_visited": ["Paris", "Lille", "Dijon"],
    },
    "Germany": {
        "total_visits": 5,
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    },
}

# Read Suttgart from the travel_log
print(travel_log["Germany"]["cities_visited"][2])