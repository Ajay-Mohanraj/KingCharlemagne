# API info link: http://www.robin-stocks.com/en/latest/functions.html
import json
import bitcoin_value as bv
import priceUpdater
import robin_stocks as r
import time
import BitcoinHelper

maxCapital = 10 # input("What is the maximum capital you are willing to invest with Charlemagne?")


infoJSON = BitcoinHelper.getJSON('./accountInfo.json')
prevPriceJSON = BitcoinHelper.getJSON('./prevPrice.json')
email = infoJSON["email"]
password = infoJSON["pass"]

r.login(email, password)

givenConstantPrice = BitcoinHelper.get_price()
print(givenConstantPrice)

#loopBreaker = input("type stop to end the loop\n")

while True:
    time.sleep(1)
    r.get_crypto_positions(info="price")
    print("Testing...", flush=True)

    #  if the current value is equal to 1% less than the constant
    if BitcoinHelper.get_price() <= givenConstantPrice * 0.99999:
        r.get_crypto_positions() #info = x
        #r.order_buy_crypto_by_quantity('BTC', 0.0001)
        print("bought " + str(BitcoinHelper.get_price()))
        #priceUpdater.updateBuy()

    # if the current value is equal to 1% more than the bought price
    for price in prevPriceJSON["boughtPrices"]:
        if BitcoinHelper.get_price() >= price * 1.0001:
            #r.order_sell_crypto_by_quantity('BTC', 0.0001)
            print("Selling " + str(price * 1.0001) + " at " + str(BitcoinHelper.get_price()))
            #priceUpdater.updateSell()


# find btc api
# https://medium.com/@randerson112358/get-bitcoin-price-in-real-time-using-python-98b7393b6152
