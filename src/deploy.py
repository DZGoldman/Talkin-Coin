import os
# from test import CoinApiTests

exit_code = os.system("python src/test.py")
if (exit_code == 0):
    os.system('git push heroku master')
else:
    print('Tests failed, deploy cancelled.')
