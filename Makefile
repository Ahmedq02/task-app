run:
	poetry run uvicorn task_app.asgi:application --reload --host 0.0.0.0 --port 8000

migrate:
	poetry run python manage.py migrate

makemigrations:
	poetry run python manage.py makemigrations

make createpasskey:
	poetry run python manage.py createpasskey

collectstatic:
	poetry run python manage.py collectstatic --noinput

test:
	poetry run python manage.py test

activate:
	poetry shell