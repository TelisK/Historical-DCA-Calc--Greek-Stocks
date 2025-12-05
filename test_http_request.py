import requests

url = "https://query1.finance.yahoo.com/v7/finance/quote?symbols=AAPL"

response = requests.get(url)
data = response.json()
print(data)
