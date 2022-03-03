import requests

response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=O763MC1G7FXSK3VL")

print(response.status_code)