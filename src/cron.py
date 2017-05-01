from slack_api import *
from coin_api_alt import CoinAPI
from db import DBClient
from slack_api import *
import sys, os

channel_id = os.environ.get('BTCHANNEL_ID') or goldman_slack_id

task = len(sys.argv) > 1 and  sys.argv[1]

def check_all_time_highs(data, log_to_slack = True):
    selected_coins = set(['btc','eth', 'xem', 'xrp', 'bcc'])
    current_val_map = {coin['symbol'].lower(): coin['price_usd'] for coin in data if coin['symbol'].lower() in selected_coins}
    db_client = DBClient()
    # db_client.seed_max_values()
    for max_value in db_client.get_all_max_vals():
        coin_id, symbol, old_ath = max_value
        current_value = float(current_val_map[symbol])
        if current_value > float(old_ath):
            db_client.update_max_value(coin_id, current_value)
            message = "<!channel> {} is at its all time high at {}!".format(symbol, str(current_value))
            if log_to_slack:
                slack.chat.post_message(channel_id, message)
            else:
                print(message)



def all_time_high():
    coin_api = CoinAPI(is_cron = True)
    coin_api.get_all_coins(check_all_time_highs)

if (task == 'ath'):
    all_time_high()
