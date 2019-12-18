# API info link: http://www.robin-stocks.com/en/latest/functions.html
import json
import bitcoin_value as bv

# parse file
def getJSON(filePathAndName):
    with open(filePathAndName, 'r') as fp:
        return json.load(fp)

info = getJSON('./accountInfo.json')
prevPrice = getJSON('./prevPrice.json')

import robin_stocks as r

# email = input("Enter you Robinhood account email: \n")
# password = input("Enter your Robinhood account password: \n")

email = info.get("email")
password = info.get("pass")

prevPrice = prevPrice.get("previousPrice")
initialPrice = prevPrice.get("initialPrice")

r.login(email, password)

# Buy order
# r.order_buy_crypto_by_quantity('BTC', 0.001)

# Sell order
# r.order_sell_crypto_by_quantity('BTC', 0.0001)

# set initial price
initialPrice = bv.USD()

# Actual algorithm loop
bool = true;

while (bool):
    in = input("Enter stop to end the crypto trader.")

    if (in == "stop"):
        bool = false;
        break

    if ((initialPrice * 0.99) == bv.USD())


# get price
print(bv.USD())

# r.load_account_profile(login)
print("Bitcoin was bought at: ")
r.crypto.get_crypto_info('BTC')
print("You now hold: ")
r.crypto.get_crypto_positions()
# r.logout()
