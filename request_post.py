import requests


url = 'http://127.0.0.1:5000/'

# data = {'symbol': 'BTCUSDT'}
data = {'symbol': 'ETHUSDT'}
response = requests.post(url, json=data)
print(response.text)
