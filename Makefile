runserver:
	poetry run python manage.py runserver

migrate:
	poetry run python manage.py migrate

makemigrations:
	poetry run python manage.py makemigrations

test:
	poetry run python manage.py test

activate:
	poetry shell