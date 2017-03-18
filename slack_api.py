from slacker import Slacker
from websocket import WebSocketApp
from coin_api import *
import json
coin_bot_token = os.environ['coin_bot_token']
slack = Slacker(coin_bot_token)

def get_socket_url(then = lambda x: x, fail = lambda x: x):
    res = requests.get('https://slack.com/api/rtm.start', params= {'token': coin_bot_token})
    if res.ok and res.json()['url']:
        return then(res.json()['url'])
    else:
        print(fail( res.error))

def on_message(ws, message):
    # print('message', message)
    res = (json.loads(message))
    if res['type'] == 'message':
        text = res['text']
        if '<@U4M1ECAMU>' in text:
            channel = res['channel']
            coin_data = get_data(get_stats(text))
            print(coin_data)
        # slack.chat.post_message(channel, get_data( get_stats(text)))

def connect():
    ws = WebSocketApp(get_socket_url(),
                                on_message = on_message
                                )
    ws.run_forever()
