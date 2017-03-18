
import requests, datetime, os

def get_data (success=lambda x:x, fail=lambda x:x):
    base_url = 'https://coinmarketcap-nexuist.rhcloud.com/api/all'
    res = requests.get(base_url)
    return success(res.json()) if res.ok else fail(res.error)


def get_stats (target):
    def closure(data):
        words = target.lower().split(' ')
        for word in words:
             if word in data:
                 coin = data[word]
                 break
             elif word in long_names:
                 coin = data[long_names[word]]
                 break
        else:
            return "Bro do you even talk coin?"
        return '''
    coin: %s
    value: %s
    volume: %s
    24-hour change: %s
    time: %s
                ''' %(coin['name'],
                '$' + str(coin['price']['usd']),
                coin['volume']['usd'], coin['change'], make_readable_time(coin['timestamp']))

    return closure

def biggest_change (data):
    max_coin = max([coin for coin in data],key=  lambda coin: data[coin]['change'] if data[coin]['change']!='?' else '-10000'  )
    return max_coin, data[max_coin]['change']

def make_readable_time (ts):
    return datetime.datetime.fromtimestamp(
        float(ts)
    ).strftime('%Y-%m-%d %H:%M:%S')
# init
def symbols_names_map(data):
    return { data[key]['name'].lower(): key for key in data if 'name' in data[key]}
long_names = get_data(symbols_names_map)
