import requests

data = 'ETHUSDT'
url = f'http://127.0.0.1:8100/api/info?symbol={data}'
response = requests.get(url)

