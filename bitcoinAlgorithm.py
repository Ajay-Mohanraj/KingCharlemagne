# API info link: http://www.robin-stocks.com/en/latest/functions.html
import json
import bitcoin_value as bv
import priceUpdater
import robin_stocks as r
import time

def getJSON(filePathAndName):
    with open(filePathAndName, 'r') as fp:
        return json.load(fp)


infoJSON = getJSON('./accountInfo.json')
prevPriceJSON = getJSON('./prevPrice.json')

email = infoJSON["email"]
password = infoJSON["pass"]

# r.login(email, password)

givenConstantPrice = "" + bv.USD()

loopBreaker = input("type stop to end the loop\n")

while True:
    time.sleep(1)

    if loopBreaker == 'stop':
        break

    #  if the current value is equal to 1% less than the constant
    if bv.USD() == int(givenConstantPrice) * 0.99:
        r.order_buy_crypto_by_quantity('BTC', 0.0001)
        priceUpdater.updateBuy()

    # if the current value is equal to 1% more than the bought price
    for price in prevPriceJSON["boughtPrices"]:
        if bv.USD() == int(price) * 1.01:
            r.order_sell_crypto_by_quantity('BTC', 0.0001)
            priceUpdater.updateSell()
