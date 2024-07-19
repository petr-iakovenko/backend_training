import requests

url = 'http://127.0.0.1:8100/'
data = {'symbol': 'XRPUSDT'}
response = requests.post(url, json=data)

