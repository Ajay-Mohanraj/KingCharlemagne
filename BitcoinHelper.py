from bs4 import BeautifulSoup
import requests
import json
import re

def get_access():
    url = 'https://robinhood.com/crypto/BTC'
    req = requests.get(url)
    m = re.search('\swindow.auth\s*=\s*(.+);', req.text)
    data = json.loads(m.group(1))
    return '{0} {1}'.format(data['token_type'], data['access_token'])

def get_unauth_price(head):
    urldomain = 'https://api.robinhood.com/marketdata/forex/quotes/3d961844-d360-45fc-989b-f6fca761d511/'
    request = requests.get(urldomain, headers=head)
    info = request.json()
    price = info.get('mark_price')
    return float(price)
def get_price():
    token = get_access()
    price = get_unauth_price({'authorization': token})
    return price



# returns JSON given file path and name
def getJSON(filePathAndName):
    with open(filePathAndName, 'r') as fp:
        return json.load(fp)
