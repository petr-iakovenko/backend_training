from datetime import datetime, timezone
import requests


def info_binance(ticket_name):
    """
    Get information from API Binance and transformation
    :return json with date
    """
    r = requests.get('https://api.binance.com//api/v3/ticker/24hr', params=ticket_name)
    current_time = f'{(datetime.now(timezone.utc)).strftime("%Y-%m-%d %H:%M:%S")} UTC+0'
    data_crypto = r.json()
    list_to_del = [
        'priceChange'
        , 'priceChangePercent'
        , 'lastPrice'
        , 'lastQty'
        , 'bidPrice'
        , 'bidQty'
        , 'askPrice'
        , 'askQty'
        , 'openPrice'
        , 'volume'
        , 'quoteVolume'
        , 'firstId'
        , 'lastId'
        , 'count'
        , 'openTime'
        , 'closeTime'
    ]  # keys for remove from getting Binance json

    for key in list_to_del:
        data_crypto.pop(key)
    data_crypto['date_info'] = current_time
    return data_crypto



# task1 - verification user
# for verification
# 8u0vlUoYGo3SlJupzgeOAsKBO5msZZGRxRR2lmqGezkhArKZTo1vh1tLetkKZgHj admin
# 8a95kCWzUcRyVfP7C2csyoLOTGgb7VCsmkRcXgkK8lLEyGqS44qVl879h4AcWV51 user
# iUh7L79I6TogSdILDZitZB8DWFI0yjugjDYEpvCxZE3xETvaJDUJypwLj7BwG0yK user

