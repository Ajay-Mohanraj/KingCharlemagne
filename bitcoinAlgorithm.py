# API info link: http://www.robin-stocks.com/en/latest/functions.html
import json
import bitcoin_value as bv
import priceUpdater
import robin_stocks as r
import time
import BitcoinHelper


infoJSON = BitcoinHelper.getJSON('./accountInfo.json')
prevPriceJSON = BitcoinHelper.getJSON('./prevPrice.json')
email = infoJSON["email"]
password = infoJSON["pass"]

# r.login(email, password)

givenConstantPrice = BitcoinHelper.getPrice()

loopBreaker = input("type stop to end the loop\n")

while loopBreaker != 'stop':
    time.sleep(30)

    #  if the current value is equal to 1% less than the constant
    if BitcoinHelper.getPrice() <= givenConstantPrice * 0.99:
        r.order_buy_crypto_by_quantity('BTC', 0.0001)
        priceUpdater.updateBuy()

    # if the current value is equal to 1% more than the bought price
    for price in prevPriceJSON["boughtPrices"]:
        if BitcoinHelper.getPrice() >= price * 1.01:
            r.order_sell_crypto_by_quantity('BTC', 0.0001)
            priceUpdater.updateSell()

# find btc api
# https://medium.com/@randerson112358/get-bitcoin-price-in-real-time-using-python-98b7393b6152
