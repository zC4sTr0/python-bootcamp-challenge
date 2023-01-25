totalbids = {}
nextBidderAvaiable = True


def addBid(name, price):
    newBid = {name, price}
    totalbids[name] = price


while (nextBidderAvaiable):
    name = input("Tell me your name: ")
    price = input("Tell your bid price")
    addBid(name, price)
    checkToContinue = input("is there any more bidders? type yes or no")
    if (checkToContinue == "yes"):
        nextBidderAvaiable = True
    else:
        nextBidderAvaiable = False

biggestBid = 0
biggestBidderName = ""
for bidderName in totalbids:
    print(totalbids[bidderName])
    if (int(totalbids[bidderName]) > int(biggestBid)):
        biggestBid = totalbids[bidderName]
        biggestBidderName = bidderName

print(f"the biggest bid is from: {biggestBidderName} of price {biggestBid}")
