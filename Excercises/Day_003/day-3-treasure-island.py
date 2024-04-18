# Escape Island Simple Game

print('''
                                                    ____
                                         v        _(    )
        _ ^ _                          v         (___(__)d
       '_|V| `
       ' oX`
          X                            v
          X             -HELP!
          X                                                 .
          X       ||O||                                     ||
          X.a##a.   M                                       |_|
       .aa########a.>>                                    __|__
    .a################aa.                                 |   |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
''')

print("Welcome to an Escape Island Game!")
print("Your mission is to escape the island.")

chosen_direction = (input("Would you like to go 'left' or 'right'?: ")).lower()
if chosen_direction == "right":
    print("Sorry, game is over.")
elif chosen_direction == "left":
    chosen_action = (input("Would you like to 'swim' or 'wait'?: ")).lower()
    if chosen_action == "swim":
        print("Sorry, game is over.")
    elif chosen_action == "wait":
        chosen_door = (input("Which door do you want to go through, 'red', 'blue' or 'yellow'?: ")).lower()
        if (chosen_door == "red") or (chosen_door == "blue"):
            print("Sorry, game is over.")
        elif chosen_door == "yellow":
            print("You win!")
        else:
            print("Sorry, game is over.")
    else:
        print("Sorry, game is over.")
else:
    print("Sorry, game is over.")
