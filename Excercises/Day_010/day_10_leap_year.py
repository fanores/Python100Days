##################################################
# Python Functions - Leap Year Exercise
##################################################
# This is how you work out whether if a particular year is a leap year. 
# - on every year that is divisible by 4 with no remainder
# - except every year that is evenly divisible by 100 with no remainder 
# - unless the year is also divisible by 400 with no remainder   
##################################################

# Leap year logic
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
      return False

# Determine the leap year
print(f"2000: {is_leap_year(2000)}")
print(f"2100: {is_leap_year(2100)}")
print(f"2400: {is_leap_year(2400)}")
print(f"1989: {is_leap_year(1989)}")
