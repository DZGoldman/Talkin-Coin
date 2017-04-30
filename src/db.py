import pymysql, os
class DBClient():
    def __init__ (self):
        self.connection = pymysql.connect(
            host = os.environ.get('DB_HOST') or  'localhost',
            user = os.environ.get('DB_USERNAME') or 'root',
            password= os.environ.get('DB_PASSWORD') or os.environ.get('PWORD'),
            db = os.environ.get('DB_DATABASE') or 'TalkinCoin'
            )

    def get_all_max_vals(self):
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM MaxValues")
            return [val for val in cursor]

    def update_max_value(self, coin_id, new_value):
        with self.connection.cursor() as cursor:
            cursor.execute(
            '''
            UPDATE MaxValues
            SET max_val = {value}
            WHERE id = {id}
            '''.format(id=coin_id, value=new_value)
            )
            self.connection.commit()

    def seed_max_values(self):
        with self.connection.cursor() as cursor:
            cursor.execute('DELETE FROM MaxValues')
            coins = [('eth', 0), ('btc', 0), ('xem', 0), ('xrp', 0)]
            for coin in coins:
                name, max_val = coin
                cursor.execute(
                    '''
                    INSERT INTO MaxValues (coin_name, max_val)
                    VALUES ('{}', {})
                    ''' .format(name, str(max_val))
                )
            self.connection.commit()
