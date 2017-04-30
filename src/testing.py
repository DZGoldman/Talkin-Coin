import os
# from test import CoinApiTests

exit_code = os.system("make test")
if (exit_code == 0):
    os.system('git push heroku master')
