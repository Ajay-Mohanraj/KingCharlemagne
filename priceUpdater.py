import json
import BitcoinHelper
# https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/


def updateBuy(possibleBuy):
    rawJSON = BitcoinHelper.getJSON('./prices.json')
    rawJSON["boughtPrices"].append(possibleBuy)
    rawJSON["quantity"] += BitcoinHelper.getBuyConstant()
    rawJSON["capital"] -= (possibleBuy * BitcoinHelper.getBuyConstant())
    BitcoinHelper.overwriteJSON(rawJSON)


def updateSell(price, currentPrice):
    rawJSON = BitcoinHelper.getJSON('./prices.json')
    if price in rawJSON["boughtPrices"]:
        rawJSON["boughtPrices"].remove(float(price))
    else:
        print("The program is not selling. There was an issue. You should probably go away now.")
    rawJSON['quantity'] -= BitcoinHelper.getBuyConstant()
    rawJSON["capital"] += (currentPrice * BitcoinHelper.getBuyConstant())
    BitcoinHelper.overwriteJSON(rawJSON)


def updateConstant(givenConstantPrice):
    rawJSON = BitcoinHelper.getJSON('./prices.json')
    rawJSON["constantPrices"].append(givenConstantPrice)
    BitcoinHelper.overwriteJSON(rawJSON)
    BitcoinHelper.setBuyConstant()
