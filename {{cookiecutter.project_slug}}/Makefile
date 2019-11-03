PYTHON := $(shell /usr/bin/env pipenv --py)
HEROKU ?= $(shell /usr/bin/env heroku 2> /dev/null)
DOCKER ?= $(shell /usr/bin/env docker 2> /dev/null)
APP := {{cookiecutter.project_slug}}
VERSION ?= $(strip $(shell cat VERSION))
COMMIT = $(strip $(shell git rev-parse --short HEAD))
BUILD_DATE = $(strip $(shell date -u +"%Y-%m-%dT%H:%M:%SZ"))
PORT ?= 8000
WORKER_PROCESSES ?= 4
TAG ?= latest
IMAGE ?= $(APP):$(TAG)

default: daemon

daemon:
	@echo "Running async daemon on 0.0.0.0:$(PORT) ..."
	@pipenv run gunicorn {{cookiecutter.project_slug}}:app --bind 0.0.0.0:$(PORT) \
		--worker-class aiohttp.worker.GunicornUVLoopWebWorker \
		--workers=$(WORKER_PROCESSES) \
		--worker-tmp-dir /dev/shm \
		--log-file=-

dev:
	@$(PYTHON) -m aiohttp.web -H localhost -P $(PORT) $(APP):build_app

tests:
	@$(PYTHON) -m pytest

analysis:
	@echo "Starting static analysis ..."
	@-pipenv run flake8
	@-pipenv run pylint --rcfile setup.cfg .
	@-pipenv run isort --check

build:
	@echo Building container ...
	@$(DOCKER) build --tag $(IMAGE) \
		--build-arg BUILD_DATE=$(BUILD_DATE) \
		--build-arg VCS_REF=$(COMMIT) \
		--build-arg VERSION=$(VERSION)\
		.

dbshell:
	@psql

deps:
ifndef HEROKU
	@curl https://cli-assets.heroku.com/install-ubuntu.sh | sh
endif
	@sudo apt-get install -y postgresql-client
	@docker-compose up postgres redis	# pgadmin4

heroku:
	@heroku create
	@heroku config:set ROOT_LOG_LEVEL=INFO
	@git push heroku master

.PHONY: default daemon dev deps tests build analysis dbshell heroku
