.PHONY: update
update:
	pip install -r requirements.txt
	python manage.py migrate

.PHONY: serve
serve:
	python manage.py runserver 0.0.0.0:8000
