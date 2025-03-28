
print("---------------------- Welcome to Silent Auction.-------------------")

holder_Names = {}

higestBid = 0
higestBidder = ""

auctionRunning = True
bid = 0

while(auctionRunning):
    name = input("What is your full name : ")

    try:
        bid = int(input("Enter your bid : "))
    except Exception:
        print("You didn't entered amount correctly so you lost already.")
        bid = 0

    holder_Names[name] = bid

    choice = input("Are there any more bidder? (y/n) : ")

    if(choice == 'n'):
        auctionRunning = False
    else:
        print("\n" * 20)
        auctionRunning = True


for bidder in holder_Names:
    if(higestBid <= holder_Names[bidder]):
        higestBid = holder_Names[bidder]
        higestBidder = bidder

print("\n" * 3)
print(f"Higest bidder is {higestBidder} with bid of {higestBid}Rs.")
