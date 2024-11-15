# Task 2
prices = {'spam': 10.0, 'duck': 12.0, 'grail': 1000.0,'shrub': 25.0, 'herring': 17.0, 'coconut': 5.0 }

pricesKeys = list(prices.keys())
pricesVals = list(prices.values())
pricesLen = len(prices)
print()

# a) Prints price of a herring.
# print(pricesKeys[4])
# print(pricesVals[4])

# b) Prints all items and their prices (do not worry about format or order).
# for pricesCount in range(0,pricesLen):
#     print( f"{pricesKeys[pricesCount]} - {pricesVals[pricesCount]}" )

# c) Prints all items and their prices, but with the following format: 
# (i) all items occupy length of 10 characters and are centred within it and 
# (ii) all prices have a total length of 8 characters with 2 digits after the decimal point. 
# For example, one line of the output will look like:
# ___duck___ costs ___12.00 gold coins
# (Note: In the line above “_” stands for a white space.)
# for pricesCount in range(0,pricesLen):
#     print( f"{pricesKeys[pricesCount]:^10} costs {pricesVals[pricesCount]:8.2f} gold coins" )

# d) Same as c) but now sort all items (keys).

# pricesKeys.sort()
# for pricesCount in range(0,pricesLen):
#     print( f"{pricesKeys[pricesCount]:^10} costs {pricesVals[pricesCount]:8.2f} gold coins" )

# e) Asks the user to enter a maximum price. Print only items that cost less or equal to
# the price the user has entered. Use the same format as in c).

maxPrice = int(input("Enter max price: "))
for pricesCount in range(0,pricesLen):
    if (pricesVals[pricesCount] <= maxPrice):
        print( f"{pricesKeys[pricesCount]:^10} costs {pricesVals[pricesCount]:8.2f} gold coins" )
