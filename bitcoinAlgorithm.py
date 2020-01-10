# API info link: http://www.robin-stocks.com/en/latest/functions.html
import json
import priceUpdater
import robin_stocks as r
import time
import BitcoinHelper


infoJSON = BitcoinHelper.getJSON('./accountInfo.json')
prevPriceJSON = BitcoinHelper.getJSON('./prices.json')
email = infoJSON["email"]
password = infoJSON["pass"]

# r.login(email, password)

givenConstantPrice = BitcoinHelper.getPrice()
priceUpdater.updateConstant(givenConstantPrice)

BitcoinHelper.setCapital(input("What is your initial capital? "))
loopBreaker = input("Type stop to end the loop\n")

while loopBreaker != 'stop' and BitcoinHelper.getCapitalLeft() > 0:
    sleep = 0
    time.sleep(30)
    sleep += 30
    possibleBuy = BitcoinHelper.getPrice()

    #  if the current value is equal to 1% less than the constant
    if BitcoinHelper.getCapitalLeft() > possibleBuy:
        if possibleBuy <= givenConstantPrice * 0.99:
            r.order_buy_crypto_by_quantity('BTC', 0.0001)
            priceUpdater.updateBuy(possibleBuy)

    # if the current value is equal to 1% more than the bought price
    for price in prevPriceJSON["boughtPrices"]:
        if possibleBuy >= price * 1.005:
            r.order_sell_crypto_by_quantity('BTC', 0.0001)
            priceUpdater.updateSell(price, possibleBuy)

    if sleep >= 10800:
        givenConstantPrice = BitcoinHelper.getPrice()
