#########################################
# Python Loops - Fizz Buzz
#########################################

# Your program should print each number from 1 to 100 in turn and include number 100.
# But when the number is divisible by 3 then instead of printing the number it should print "Fizz".
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

for number in range(1, 101):
    printed_text = ""

    if number % 3 == 0:
        printed_text = "Fizz"

    if number % 5 == 0:
        printed_text += "Buzz"

    if printed_text == "":
        printed_text = number

    print(printed_text)
