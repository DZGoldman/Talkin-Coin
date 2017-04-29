import requests, datetime, os

class CoinAPI():
    def __init__ (self):
        self.base_url =  'https://api.coinmarketcap.com/v1/ticker/'
        self.ids_to_name = self.get_all_coins(self.map_ids_to_name)
        self.names_set = {self.ids_to_name[coin_id] for coin_id in self.ids_to_name }

    def get_all_coins (self, success=lambda x:x, fail=lambda x:x):
        res = requests.get(self.base_url)
        return success(res.json()) if res.ok else fail(res.text)

    def map_ids_to_name(self, data):
        return {coin['id'].lower(): coin['name'] for coin in data}

    def get_single_coin(self, coin, success=lambda x:x, fail=lambda x:x):
        url = this.base_url+coin
        res = requests.get(url)
        return success(res.json()) if res.ok else fail(res.text)

    def get_data_main(self, text):
        pass
    def sanitize_input(self, text)
        pass

test = CoinAPI()
# print (test.names_set)
print(test.ids_to_name)
