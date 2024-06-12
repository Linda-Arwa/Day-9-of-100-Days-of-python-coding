# A secret auctioning or beading program.

import os

from art import logo
print(logo)

# Creating an empty dictionary
bidders = {}

#variable
more_bidders = True

# creating a function
def highest_bid(bids):
    highest_amount = 0
    winner = " "
    for bidder in bids:
        bidding_amount = bids[bidder]
        if bidding_amount > highest_amount:
            highest_amount = bidding_amount
            winner = bidder
    print(f"\n The winner is {winner} with a bid of {highest_amount}\n")

while more_bidders:
   
    #Asking user to input name
    name = input("Enter your name\n")

    #Asking user to input bid amount
    bid = int(input("What is your bid amount\n"))

    # The bidders dictionary
    bidders[name] = bid
    
    # More bidders
    
    more_people = input("Is there another person going to bid? If yes type 'Yes', if no, type 'No'\n").lower()
    if more_people == "no":
        more_bidders = False
        highest_bid(bidders)
    elif more_people == "yes":
        os.system('cls') # for clearing the console 
    else:
        print("Please enter yes to continue or no to stop")
        #os.system('cls')
        
#print(bidders)
