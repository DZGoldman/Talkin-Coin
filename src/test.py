import unittest, time, os, requests, sys
from coin_api_alt import CoinAPI
from cron import all_time_high
from db import DBClient



class CoinApiTests(unittest.TestCase):
    def setUp(self):
        self.coin_api = CoinAPI()
        time.sleep(1)

    def test_new(self):
        coin_api = self.coin_api
        self.assertTrue( len(coin_api.ids_to_name.keys() ) > 800 )
        self.assertTrue('ethereum' in coin_api.names_set)
        self.assertTrue('eth' in coin_api.ids_to_name)

    def test_sanitize(self):
        self.assertFalse(self.coin_api.sanitize_input(''))
        self.assertEqual(  self.coin_api.sanitize_input('sho@#@$w @#$me e@#$t#$!!h!'), 'show me eth')

    def test_extract_coin_from_text(self):
        extract = self.coin_api.extract_coin_from_text
        self.assertFalse(extract(''))
        self.assertEqual( extract('I want BITCOIN! stats'), 'bitcoin')
        self.assertEqual( extract('I want btC! stats'), 'bitcoin')
        self.assertFalse(extract('there are no coins in here'))

    def test_prettify(self):
        self.assertFalse(self.coin_api.prettify_data({}))

    def test_main(self):
        self.assertEqual(self.coin_api.get_data_main('No coins in here'), self.coin_api.not_found_message)
        time.sleep(1)
        eth_result = self.coin_api.get_data_main('eth please')
        print(eth_result)
        self.assertTrue('ethereum' in eth_result and 'market_cap_usd' in eth_result)

class DBTests(unittest.TestCase):
    def test_db_connect(self):
        self.assertTrue(DBClient())
        self.assertEqual(len(DBClient().get_all_max_vals()), 5)

class CronTests(unittest.TestCase):
    def test_check_all_time_high(self):
        self.assertEqual( os.system('python src/cron.py ath'), 0)
    def test_check_percent_change(self):
        self.assertEqual( os.system('python src/cron.py pc'), 0)


res = requests.get("https://coinmarketcap-nexuist.rhcloud.com/api")
if res.status_code ==200:
    unittest.main(verbosity=2)
else:
    print("Failed to connect to coin api" )
    print(res.text)
    sys.exit(1)
