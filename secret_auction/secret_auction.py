import os
from gavel_art import logo
clear = lambda: os.system('clear')

print(logo)
print('Welcome to the secret auction for the exclusive ultimate Tesla')
bidder_dict = {}

def start_auction(name, bid):
    bidder_dict[name] = bid

more_users = True
while more_users:
    user_name = input('Please state your name: ').capitalize()
    user_bid = int(input('Place your bid: $'))
    start_auction(user_name, user_bid)
    more_bidders = input('Are there more bidders? (yes) or (no): ').lower()
    if more_bidders == 'yes':
        clear()
    else:
        more_users = False

max_bid = 0
for key in bidder_dict:
    if bidder_dict[key] > max_bid:
        max_bid = bidder_dict[key]

print(f"The winner is {max(bidder_dict)} with a bid of ${max_bid}!")

# Algorithm
# Create new dictionary
# Ask user to input name and bid
# Append results
# Ask user if there is another user
# if other_user == True repeat.
# else clear console
# Loop through list and return the highest bid.
    