from flask import Flask, request
import os, json
from slacker import Slacker
from slack_api import *
from coin_api_alt import CoinAPI

webhook_token = os.environ['webhook_token']

app = Flask(__name__)

if __name__ =='__main__':
    coin_api = CoinAPI()

@app.route('/', methods=['Post'])
def recieve():

    data = request.form
    print('----- request recieved ------', data)
    if data.get('token') == webhook_token:
        text, user_id, channel_id = data.get('text'), data.get('user_id'), data.get('channel_id')
        print('-----text -----', text)
        print(channel_id)
        user_tag = user_tag = "<@%s>" %(user_id)
        slack.chat.post_message(channel_id, user_tag + ' ' + coin_api.get_data_main(text))
        return 'done'
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port)
