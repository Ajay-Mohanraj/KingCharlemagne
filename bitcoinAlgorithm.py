# API info link: http://www.robin-stocks.com/en/latest/functions.html
import json
import bitcoin_value as bv

CAPITAL_VARIABLE = 10

# loop delay import
import time

# parse file
def getJSON(filePathAndName):
    with open(filePathAndName, 'r') as fp:
        return json.load(fp)

infoJSON = json.loads(open('./accountInfo.json').read())
prevPriceJSON = json.loads(open('./prevPrice.json').read())

import robin_stocks as r

# email = input("Enter you Robinhood account email: \n")
# password = input("Enter your Robinhood account password: \n")

email = infoJSON["email"]
password = infoJSON["pass"]

prevPrice = prevPriceJSON["previousPrice"]
print(prevPrice)

initialPrice = prevPriceJSON["initialPrice"]
print(initialPrice)

capitalLeft = prevPriceJSON["availableCapitol"]

capitalLeft = CAPITAL_VARIABLE

print(capitalLeft)

r.login(email, password)

# Buy order
# r.order_buy_crypto_by_quantity('BTC', 0.001)

# Sell order
# r.order_sell_crypto_by_quantity('BTC', 0.0001)

# set initial price
initialPrice = bv.USD()
print(initialPrice)

# Actual algorithm loop
bool = True;

stop = ""#input("Enter 's' to end the crypto trader.")

count = 1

# this loop is not working properly from some reason
while (stop != "s"):
    time.sleep(1)
    #print("hi",flush=True)
    prevPrice = bv.USD()

    if (capitalLeft > 0):
        if (initialPrice * 0.99999 >= int(prevPrice)):
            print("Bitcoin would have been bought at: " + prevPrice + " after it dropped from " + initialPrice, flush=True)

    #if ((int(initialPrice) * 0.99) == bv.USD())


# get price
print(bv.USD())

# r.load_account_profile(login)
print("Bitcoin was bought at: ")
r.crypto.get_crypto_info('BTC')
print("You now hold: ")
r.crypto.get_crypto_positions()
# r.logout()
