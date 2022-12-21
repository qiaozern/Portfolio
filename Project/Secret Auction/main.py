from replit import clear
print("Welcome to the secret auction.")

bid = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # bidding_record = {"A":123, "B":234}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"the winner is {winner} with a bid of ${highest_bid}.")

while not bidding_finished:
    bid_name = input("What is your name?: ")
    bid_price = int(input("What's your bid?: $"))

    # add name and bid price into "bid" dictionary
    bid[bid_name] = bid_price

    next_bidder = input("Are there any other bidders? Type 'yes' or 'no").lower()

    # condition continue the auction
    if next_bidder == 'no':
        bidding_finished = True
        find_highest_bidder(bid)
    elif next_bidder == 'yes':
        clear()
        
