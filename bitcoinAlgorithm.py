# API info link: http://www.robin-stocks.com/en/latest/functions.html
import json
import bitcoin_value as bv

# loop delay import
import time

# parse file
def getJSON(filePathAndName):
    with open(filePathAndName, 'r') as fp:
        return json.load(fp)

info = json.loads(open('./accountInfo.json').read())
prevPrice = json.loads(open('./prevPrice.json').read())

import robin_stocks as r

# email = input("Enter you Robinhood account email: \n")
# password = input("Enter your Robinhood account password: \n")

email = info["email"]
password = info["pass"]

prevPrice = prevPrice["previousPrice"]
print(prevPrice)\
# The intitial Price is off for some reason
initialPrice = prevPrice[0]
print(initialPrice)

r.login(email, password)

# Buy order
# r.order_buy_crypto_by_quantity('BTC', 0.001)

# Sell order
# r.order_sell_crypto_by_quantity('BTC', 0.0001)

# set initial price
initialPrice = "" + bv.USD()

# Actual algorithm loop
bool = True;

stop = ""#input("Enter 's' to end the crypto trader.")

count = 1

# this loop is not working properly from some reason
while (stop != "s"):
    time.sleep(1)
    print("hi",flush=True)

    #if ((int(initialPrice) * 0.99) == bv.USD())


# get price
print(bv.USD())

# r.load_account_profile(login)
print("Bitcoin was bought at: ")
r.crypto.get_crypto_info('BTC')
print("You now hold: ")
r.crypto.get_crypto_positions()
# r.logout()
