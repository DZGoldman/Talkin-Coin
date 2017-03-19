from flask import Flask, request
import os, json
from slacker import Slacker
from coin_api import *

webhook_token = os.environ['webhook_token']
coin_bot_token = os.environ['coin_bot_token']
goldman_slack_id = os.environ['goldman_slack_id']

slack = Slacker(coin_bot_token)

app = Flask(__name__)

@app.route('/', methods=['Post'])
def recieve():

    data = request.form
    if data.get('token') == webhook_token:
        print('----------passed')
        text, user_id, channel_id = data.get('text'), data.get('user_id'), data.get('channel_id')
        print('-------text')
        print(text)
        user_tag = user_tag = "<@%s>" %(user_id)
        slack.chat.post_message(channel_id, user_tag + ' ' + get_data( get_stats(text)))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    slack.chat.post_message(goldman_slack_id, 'starting server connecting')
    app.run(host='0.0.0.0', port=port)
