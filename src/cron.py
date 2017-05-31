from slack_api import *
from coin_api_alt import CoinAPI
from db import DBClient
from slack_api import *
import sys, os

channel_id = os.environ.get('BTCHANNEL_ID') or goldman_slack_id

task = len(sys.argv) > 1 and  sys.argv[1]

def check_all_time_highs(data, log_to_slack = True):
    db_client = DBClient()
    all_max_vals = db_client.get_all_max_vals()
    selected_coins = {max_val[1] for max_val in all_max_vals}
    current_val_map = {coin['symbol'].lower(): coin['price_usd'] for coin in data if coin['symbol'].lower() in selected_coins}
    # db_client.seed_max_values()
    for max_value in all_max_vals:
        coin_id, symbol, old_ath = max_value
        current_value = float(current_val_map[symbol])
        if current_value > float(old_ath):
            db_client.update_max_value(coin_id, current_value)
            message = "<!channel> {} is at its all time high at {}!".format(symbol, str(current_value))
            if log_to_slack:
                slack.chat.post_message(channel_id, message)
            else:
                print(message)
def check_percent_change(data):
    db_client = DBClient()
    all_max_vals = db_client.get_all_max_vals()
    selected_coins = {max_val[1] for max_val in all_max_vals}
    current_val_map = {coin['symbol'].lower(): coin['percent_change_24h'] for coin in data if coin['symbol'].lower() in selected_coins}
    for coin in current_val_map:
        percent = current_val_map[coin]
        if float(percent) > 10:
            slack.chat.post_message(channel_id, '<!channel> {} increased by {}% in the past 24 hours.'.format(coin, percent))
        elif float(percent) < -10:
            slack.chat.post_message(channel_id, '<!channel> {} decreased by {}% in the past 24 hours.'.format(coin, percent))


    pass

def percent_change():
    coin_api = CoinAPI(is_cron = True)
    coin_api.get_all_coins(check_percent_change)

def all_time_high():
    coin_api = CoinAPI(is_cron = True)
    coin_api.get_all_coins(check_all_time_highs)

if (task == 'ath'):
    all_time_high()
elif task == 'pc':
    percent_change()
