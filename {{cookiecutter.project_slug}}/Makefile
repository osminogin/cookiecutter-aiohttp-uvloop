PYTHON = $(/usr/bin/env pipenv --py)
HEROKU ?= $(shell /usr/bin/env heroku 2> /dev/null)
DOCKER ?= $(shell /usr/bin/env docker 2> /dev/null)
APP := '{{cookiecutter.project_slug}}'
VERSION ?= $(strip $(shell cat VERSION))
COMMIT = $(strip $(shell git rev-parse --short HEAD))
BRANCH = $(strip $(shell git rev-parse --abbrev-ref HEAD))
TAG ?= latest
IMAGE ?= eu.gcr.io/$(APP)/$(APP):$(TAG)

default: daemon

daemon:
	@echo "Running async daemon ..."
	@pipenv run gunicorn {{cookiecutter.project_slug}}:app --bind localhost:8000 \
		--worker-class aiohttp.worker.GunicornUVLoopWebWorker

test:
	@pipenv run pytest

analysis:
	@echo "Starting static analysis ..."
	@-pipenv run flake8
	@-pipenv run pylint --rcfile setup.cfg .
	@-pipenv run isort --check

build:
	@echo Building container ...
	@docker build -t $(IMAGE) .

dbshell:
	@psql

deps:
ifndef HEROKU
	@curl https://cli-assets.heroku.com/install-ubuntu.sh | sh
endif
	@sudo apt-get install -y postgresql-client
	@docker-compose up postgres redis	# pgadmin4

.PHONY: default daemon deps test build analysis dbshell
