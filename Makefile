
source_db: virtenv
	bash -c "source virtenv/bin/activate; make db.sqlite3"

virtenv:
	virtualenv virtenv


virtenv/lib/python2.7/site-packages/django:
	pip install Django

virtenv/lib/python2.7/site-packages/unicodecsv:
	pip install unicodecsv

virtenv/lib/python2.7/site-packages/suit:
	pip install django-suit

install: virtenv/lib/python2.7/site-packages/suit virtenv/lib/python2.7/site-packages/unicodecsv virtenv/lib/python2.7/site-packages/django
	echo "All Libraries installed."

clean:
	rm -rf virtenv db.sqlite3

db.sqlite3: install
	python manage.py makemigrations
	python manage.py migrate
	python manage.py createsuperuser


run_sourced: 
	python manage.py runserver
	
