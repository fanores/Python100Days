##################################################
# Python Functions with Outputs
##################################################

# Simple function
def my_simple_function(some_input_variable):
    # Do this with some_input_variable
    # Do that with some_input_variable
    # Then return something
    pass

# Function with outputs
def my_function_with_output(some_input_variable):
    # Do this with some_input_variable
    output = some_input_variable
    # Then return something
    return output

# Function to format a name as title case
def format_name_as_title_case(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

print(format_name_as_title_case("johN", "dOe"))

# Function as input parameter of another function
def my_first_function(text):
    output = text.lower()
    return output

def my_second_function(text):
    output = text.title()
    return output

print(my_second_function(my_first_function("hELLO pYtHoN")))