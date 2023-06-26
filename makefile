PORT ?= 8000

runserver:
	@echo "Starting Django server..."
	@poetry run python manage.py runserver $(PORT)
