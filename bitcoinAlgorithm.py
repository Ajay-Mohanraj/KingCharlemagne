# API info link: http://www.robin-stocks.com/en/latest/functions.html
import json
import bitcoin_value as bv
import priceUpdater

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

boughtPrice = prevPriceJSON["boughtPrice"]
print(boughtPrice)
# The intitial Price is off for some reason
givenConstantPrice = prevPriceJSON["givenConstantPrice"]
print(givenConstantPrice)

r.login(email, password)

# Buy order
# r.order_buy_crypto_by_quantity('BTC', 0.001)

# Sell order
# r.order_sell_crypto_by_quantity('BTC', 0.0001)

# set initial price
givenConstantPrice = "" + bv.USD()

# Actual algorithm loop
bool = True

stop = ""#input("Enter 's' to end the crypto trader.")

count = 1

# this loop is not working properly from some reason
while (stop != "s"):
    time.sleep(1)
    print("hi",flush=True)

    #  if the current value is equal to 1% less than the constant
    if bv.USD() == int(givenConstantPrice) * 0.99:
        r.order_buy_crypto_by_quantity('BTC', 0.0001)
        priceUpdater.updateJSON()

    # if the current value is equal to 1 % more than the bought price
    if bv.USD() == boughtPrice * 1.01:
        r.order_sell_crypto_by_quantity('BTC', 0.0001)
        priceUpdater.updateJSON()


# get price
print(bv.USD())

# r.load_account_profile(login)
print("Bitcoin was bought at: ")
r.crypto.get_crypto_info('BTC')
print("You now hold: ")
r.crypto.get_crypto_positions()
# r.logout()
