init:
	pip install -r requirements.txt

test:
	brew services start mysql
	python src/test.py
	brew services stop mysql

db_setup:
	python src/set_up_db.py

start:
	python src/main.py

ath:
	python src/cron.py ath

pc:
	python src/cron.py pc

enter_db:
	python src/enter_db.py
