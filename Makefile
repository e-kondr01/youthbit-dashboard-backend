.PHONY: up
up:
	docker compose up --build

.PHONY: run
run: up

.PHONY: local
local:
	docker compose -f local-docker-compose.yml up -d
	python django_core/manage.py migrate
	python django_core/manage.py runserver

.DEFAULT_GOAL := up
