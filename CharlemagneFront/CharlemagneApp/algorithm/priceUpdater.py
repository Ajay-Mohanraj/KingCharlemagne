import json
import BitcoinHelper
# https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/


def updateBuy(possibleBuy):
    rawJSON = BitcoinHelper.getJSON('./prices.json')
    rawJSON["boughtPrices"].append(possibleBuy)
    rawJSON["quantity"] += 0.0001
    rawJSON["capital"] -= possibleBuy
    BitcoinHelper.overwriteJSON(rawJSON)


def updateSell(price, currentPrice):
    rawJSON = BitcoinHelper.getJSON('./prices.json')
    rawJSON["boughtPrices"].remove(price)
    rawJSON['quantity'] -= 0.0001
    rawJSON["capital"] += int(currentPrice)
    BitcoinHelper.overwriteJSON(rawJSON)


def updateConstant(givenConstantPrice):
    rawJSON = BitcoinHelper.getJSON('./prices.json')
    rawJSON["constantPrices"].append(int(givenConstantPrice))
    BitcoinHelper.overwriteJSON(rawJSON)

