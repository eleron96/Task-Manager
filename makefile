PORT ?= 8000

runserver:
	@echo "Starting Django server..."
	@poetry run python manage.py runserver $(PORT)


translate:
	@echo "Translating..."
	@poetry run python manage.py makemessages -l ru
	@poetry run python manage.py compilemessages

lint:
	@poetry run flake8 task_manager

test:
	poetry run coverage run --source=app,labels,status,task_manager,tasks -m pytest

report:
	poetry run coverage report -m --omit=venv/*
