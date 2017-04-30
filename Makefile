init:
	pip install -r requirements.txt

test:
	python src/test.py
	say 'yo'
	
db_setup:
	python src/set_up_db.py

start:
	python src/main.py

ath:
	python src/cron.py ath
