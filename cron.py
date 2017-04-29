from slack_api import *
from coin_api_alt import CoinAPI
def send_eth_price (data):
    coin_api_alt = CoinAPI(cron_data = True)
get_single_coin('eth', send_eth_price)
