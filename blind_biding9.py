#This is a blind Binding auction game. Here, bidders bids blindly wothout knowing the price of other bidders and the highest one wins.

import os

def clear_screen():
    os.system('cls')


from blind_art9 import logo
print(logo)

print("Welcome to Secret Auction Program!")

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if (int(bid_amount) > int(highest_bid)):
      highest_bid = bid_amount
      winner = bidder
  print(f"The highest bidder is {winner} with the bid amount of ${highest_bid}")
  

while not bidding_finished:
  name = input("What is your name?")
  price = input("What is your bid? $")
  bids[name] = price
  should_continue = input("Are there any other bidders? Type yes or no.")
  if should_continue == 'no':
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == 'yes':
    clear_screen()
