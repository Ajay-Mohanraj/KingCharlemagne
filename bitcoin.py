# get value of bitcoin from https://robinhood.com/crypto/BTC using BeautifulSoup
from bs4 import BeautifulSoup
import requests


def getPrice():
    price = ""

    response = requests.get("https://robinhood.com/crypto/BTC")  # Returns instance of Response class
    response.encoding = 'utf-8'  # Just in case the charset of response is not recognized

    # crypto: bs4.BeautifulSoup = BeautifulSoup(response.content, 'html.parser')
    # annotation format highlights what type of class the variable crypto is
    # https://stackoverflow.com/questions/51639332/use-of-colon-in-variable-declaration
    crypto = BeautifulSoup(response.content, "html.parser")

    for digit in crypto.find_all("span", {"class": "_9YsRP4ChsxbL9qzZnKv0K up"}):  # return type of find is object
        if digit.text != '$' and digit.text != ',':
            price += digit.text

    return float(price)
