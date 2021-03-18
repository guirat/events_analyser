RUNPIPENV :=pipenv run
MANAGE := python manage.py

install:
	pip install pipenv
	pipenv install

migrations:
	$(RUNPIPENV) $(MANAGE) makemigrations

migrate:
	$(RUNPIPENV) $(MANAGE) migrate

run: migrate
	$(RUNPIPENV) $(MANAGE) runserver 8000

test:
	$(RUNPIPENV) pytest

format:
	$(RUNPIPENV) black .

lint:
	$(RUNPIPENV) flake8 --doctests .