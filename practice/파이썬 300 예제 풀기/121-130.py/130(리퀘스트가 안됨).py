import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

print(btc)
