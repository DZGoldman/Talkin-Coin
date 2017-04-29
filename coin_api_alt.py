import requests, datetime, os
import re
from IPython import embed
class CoinAPI():
    def __init__ (self):
        self.base_url =  'https://api.coinmarketcap.com/v1/ticker/'
        self.ids_to_name = self.get_all_coins(self.map_ids_to_name)
        self.names_set = {self.ids_to_name[coin_id].lower() for coin_id in self.ids_to_name }
        self.not_found_message = 'No Coins Dumbass'

    def get_all_coins (self, success=lambda x:x, fail=lambda x:x):
        res = requests.get(self.base_url)
        return success(res.json()) if res.ok else fail(res.text)

    def map_ids_to_name(self, data):
        return {coin['symbol'].lower(): coin['name'].lower() for coin in data}

    def get_single_coin(self, coin, success=lambda x:x, fail=lambda x:x):
        url = self.base_url+coin
        res = requests.get(url)
        return success(res.json()) if res.ok else fail(res.text)

    def sanitize_input(self, text):
        return re.sub(r'([^\s\w]|_)+', '', text)

    def extract_coin_from_text(self, text):
        words = [   word.lower() for word in self.sanitize_input(text).split() ]
        for word in words:
            if word in self.ids_to_name:
                return self.ids_to_name[word]
            elif word in self.names_set:
                return word
        else:
            return False
    def get_data_main(self, text):
        coin = self.extract_coin_from_text(text)
        if coin:
            result = self.get_single_coin(coin)
            return str(result[0]) if len(result) else self.not_found_message
        else:
            return self.not_found_message