
build:
	docker-compose up -d --build
up:
	docker-compose up -d
kill:
	docker-compose kill
reload: kill up

bash:
	docker-compose exec web bash

migrate:
	docker-compose exec web python manage.py migrate


shell:
	docker-compose exec web python manage.py shell



l-migrate:
	python manage.py migrate

test:
	python manage.py test polls

run:
	python manage.py runserver

l-shell:
	python manage.py shell
