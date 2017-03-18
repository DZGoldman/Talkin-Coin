from slacker import Slacker
from websocket import WebSocketApp
from coin_api import *
import json, time
coin_bot_token = os.environ['coin_bot_token']
slack = Slacker(coin_bot_token)
goldman_slack_id = os.environ['goldman_slack_id']

def get_socket_url(then = lambda x: x, fail = lambda x: x):
    res = requests.get('https://slack.com/api/rtm.start', params= {'token': coin_bot_token})
    if res.ok and res.json()['url']:
        return then(res.json()['url'])
    else:
        print(fail( res.error))
def on_error(ws, error):
    print('error', error)
    error_string = json.loads(error)
    slack.chat.post_message(goldman_slack_id, error_string)
def on_close(ws):
    print('closing')
    slack.chat.post_message(goldman_slack_id, 'bot closing')
    time.sleep(30)
    connect()

def on_message(ws, message):
    res = (json.loads(message))
    if res['type'] == 'message':
        text = res['text']
        if '<@U4M1ECAMU>' in text:
            channel = res['channel']
            user = res['user']
            user_tag = "<@%s>" %(user)
            coin_data = get_data(get_stats(text))
            slack.chat.post_message(channel, user_tag + ' ' + get_data( get_stats(text)))

def connect():
    slack.chat.post_message(goldman_slack_id, 'bot connecting')
    ws = WebSocketApp(get_socket_url(),
                                on_message = on_message,
                                on_close = on_close
                                )
    ws.run_forever()
