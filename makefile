PORT ?= 8000

runserver:
	poetry run python manage.py runserver $(PORT)
