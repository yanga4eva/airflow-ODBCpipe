import requests

response = requests.get(
    "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=O763MC1G7FXSK3VL")

dailymarket = response.json()

print(dailymarket["Time Series (Daily)"]["2021-12-17"]["3. low"])
