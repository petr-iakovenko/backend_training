import requests

"""
Get information to user from DB 
"""

url = 'http://127.0.0.1:5000/api/info'
# data = {'symbol': 'BTCUSDT'}
data = {'symbol': 'ETHUSDT'}
response = requests.get(url, json=data)

print(response.json())
