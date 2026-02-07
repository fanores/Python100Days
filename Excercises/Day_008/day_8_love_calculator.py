##################################################
# Python Functions with Inputs - Love Calculator
##################################################

def calculate_love_score(name1, name2):
    combined_names = name1.lower() + name2.lower()

    t_count = combined_names.count('t')
    r_count = combined_names.count('r')
    u_count = combined_names.count('u')
    e_count = combined_names.count('e')
    first_digit = t_count + r_count + u_count + e_count

    l_count = combined_names.count('l')
    o_count = combined_names.count('o')
    v_count = combined_names.count('v')
    e_count = combined_names.count('e')
    second_digit = l_count + o_count + v_count + e_count

    love_score = int(str(first_digit) + str(second_digit))
    return love_score


# Get user input for the two names
name_person1 = input("Enter the first name: ")
name_person2 = input("Enter the second name: ")

# Calculate the love score and print the result
love_score = calculate_love_score(name_person1, name_person2)
print(f"The love score for {name_person1} and {name_person2} is: {love_score}")
