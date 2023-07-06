PORT ?= 8000

runserver:
	@echo "Starting Django server..."
	@poetry run python manage.py runserver $(PORT)


translate:
	@echo "Translating..."
	@poetry run python manage.py makemessages -l ru
	@poetry run python manage.py compilemessages