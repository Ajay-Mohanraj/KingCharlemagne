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

givenConstantPrice = BitcoinHelper.getPrice()
priceUpdater.updateConstant(givenConstantPrice)

print("------------------------------------------------------------")
print("Welcome to the Charlemagne Bitcoin Trading Bot!")
print("To begin, please enter the authentication code\nsent to your phone.")
r.login(email, password)

BitcoinHelper.setCapital(input("Next, how much money would you like to invest?"))
print("Perfect!")
loopBreaker = input("Please type 'stop' to stop the trading bot.\n")

sleep = 0

while loopBreaker != 'stop' and BitcoinHelper.getCapitalLeft() > 0:
    time.sleep(30)
    sleep += 30
    possibleBuy = BitcoinHelper.getPrice()
    print("Charlemagne is determining whether or not to buy or sell...")

    #  if the current value is equal to 1% less than the constant
    if BitcoinHelper.getCapitalLeft() > possibleBuy:
        if possibleBuy <= (givenConstantPrice * 0.999):
            r.order_buy_crypto_by_quantity('BTC', 0.0001)
            priceUpdater.updateBuy(possibleBuy)
            print("0.0001 Bitcoin was bought at: " + possibleBuy)

    # if the current value is equal to 1% more than the bought price
    for price in prevPriceJSON["boughtPrices"]:
        if possibleBuy >= price * 1.005:
            r.order_sell_crypto_by_quantity('BTC', 0.0001)
            priceUpdater.updateSell(price, possibleBuy)
            print("0.0001 Bitcoin was sold at: " + possibleBuy)

    if ((sleep % 10800) == 0):
        givenConstantPrice = BitcoinHelper.getPrice()
