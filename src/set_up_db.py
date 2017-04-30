from db import DBClient

db_client = DBClient()

db_client.create_max_val_tables()
db_client.seed_max_values()
