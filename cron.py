from slack_api import *
def send_eth_price (data):
    price  = data['price']['usd']
    print('cron: eth price', price)
    if (price < 40) or  (price > 55):
        slack.chat.post_message(goldman_slack_id, str(price))
get_single_coin('eth', send_eth_price)
