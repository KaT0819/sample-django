
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



local-migrate:
	python manage.py migrate

test:
	python manage.py test polls

run:
	python manage.py runserver

local-shell:
	python manage.py shell


heroku-init:
	heroku run python manage.py migrate

heroku-static:
	heroku run python manage.py collectstatic

heroku-log:
	heroku log --tail
