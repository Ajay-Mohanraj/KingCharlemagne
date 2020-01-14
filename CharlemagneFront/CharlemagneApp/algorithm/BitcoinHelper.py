from bs4 import BeautifulSoup
import requests
import json

#hi
def getPrice():
    KEY = getAuthKey()
    USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0'
    HEADERS = {'User-Agent': USER_AGENT, 'Origin': 'https://robinhood.com', 'Referer': 'https://robinhood.com/',
               'Host': 'api.robinhood.com', 'Authorization': KEY, 'Accept-Encoding': 'gzip,deflate,br',
               'TE': 'Trailers'}

    response = requests.get("https://api.robinhood.com/marketdata/forex/quotes/3d961844-d360-45fc-989b-f6fca761d511/", headers=HEADERS)
    responseJSON = json.loads(response.content)
    return responseJSON['ask_price']


def scrapeWeb():
    url = 'https://robinhood.com/crypto/BTC'
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    return soup


def getAuthKey():
    js_script = (scrapeWeb().select('script')[0]).text
    split_js = js_script.split('\n')
    winAuth = (split_js[28].split(":"))[1]

    # removes 13 characters from the end and strips unnecessary quotation marks
    winAuthToken = winAuth[:-13].strip('"')
    return "Bearer " + winAuthToken


# returns JSON given file path and name
def getJSON(filePathAndName):
    with open(filePathAndName, 'r') as fp:
        return json.load(fp)


# overwrites prices.json file with new information
def overwriteJSON(data):
    with open("./prices.json", 'w') as fp:
        json.dump(data, fp)


# sets capital
def setCapital(capital):
    rawJSON = getJSON('./prices.json')
    rawJSON['capital'] = int(capital)
    overwriteJSON(rawJSON)


# gets capital left
def getCapitalLeft():
    rawJSON = getJSON('./prices.json')
    return int(rawJSON['capital'])
