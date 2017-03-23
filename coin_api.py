
import requests, datetime, os

def get_data (success=lambda x:x, fail=lambda x:x):
    base_url = 'https://coinmarketcap-nexuist.rhcloud.com/api/all'
    res = requests.get(base_url)
    return success(res.json()) if res.ok else fail(res.text)

def get_single_coin(coin, success=lambda x:x, fail=lambda x:x):
    base_url = 'https://coinmarketcap-nexuist.rhcloud.com/api/'+coin
    res = requests.get(base_url)
    return success(res.json()) if res.ok else fail(res.text)
def error_logger():
    pass
def get_stats (target, full_names={}):
    def closure(data):
        words = target.lower().split(' ')
        for word in words:
             if word in data:
                 coin = data[word]
                 break
             elif word in full_names:
                 coin = data[full_names[word]]
                 break
        else:
            return "Bro do you even talk coin?"
        return '''
    coin: %s
    value: %s
    volume: %s
    market-cap: %s
    24-hour change: %s
    time: %s
                ''' %(coin['name'],
                '$' + str(coin['price']['usd']),
                '$' + str(coin['volume']['usd']),
                '$' + str(coin['market_cap']['usd']),
                coin['change'], make_readable_time(coin['timestamp']))

    return closure

def biggest_change (data):
    max_coin = max([coin for coin in data],key=  lambda coin: data[coin]['change'] if data[coin]['change']!='?' else '-10000'  )
    return max_coin, data[max_coin]['change']

def make_readable_time (ts):
    return datetime.datetime.fromtimestamp(
        float(ts)
    ).strftime('%Y-%m-%d %H:%M:%S')

def symbols_names_map(data):
    return { data[key]['name'].lower(): key for key in data if 'name' in data[key]}
