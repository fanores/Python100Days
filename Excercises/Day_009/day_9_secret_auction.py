##################################################
# Python Dictionaries - Secret Auction
##################################################

# Import gavel logo
from day_9_gavel_logo import gavel_logo

# Clear the console by printing new lines
def clear_screen():
    print("\n" * 100)

def add_participant_to_auction(auction_participants, name, bid):
    auction_participants[name] = bid

# Start auction
auction_participants = {}
is_auction_active = True

print(gavel_logo)

# Start auction loop
while is_auction_active:
    participant_name = input("Type your name:\n")
    participant_bid = int(input("Type your bid in €:\n"))
    add_participant_to_auction(auction_participants, participant_name, participant_bid)

    if input("Are there any other bidders? Type 'yes' or 'no'.\n").lower() == "yes":
        clear_screen()
    else:
        clear_screen()
        is_auction_active = False

# Report the auction result
auction_winners = []
max_bid = max(auction_participants.values())
for participant in auction_participants:
     if auction_participants[participant] == max_bid:
         auction_winners.append(f"The winner is {participant} with a bid of {auction_participants[participant]}€.")
         
for winner in auction_winners:
    print(winner)
