PROJECT_NAME = l2py
PYTHON_VERSION = 3.10

UNAME = $(shell uname)
DOCKER = $(shell which docker)
COMPOSE = $(shell which docker-compose)
POETRY = $(shell which poetry)
PYTHON = $(shell which python$(PYTHON_VERSION))

REQUIRED_PACKAGES := swig openssl


lint:
	- poetry run black . --check
	- poetry run isort -c --profile=black .


format:
	poetry run black .
	poetry run isort --profile=black .

test:
	pytest .

install_requirements:
ifeq ($(UNAME),Darwin)
	brew install openssl; \
	brew install swig; \
	export LDFLAGS="-L$(brew --prefix openssl)/lib" \
	CFLAGS="-I$(brew --prefix openssl)/include" \
	SWIG_FEATURES="-cpperraswarn -includeall -I$(brew --prefix openssl)/include"
endif

install: install_requirements
	$(info Installing poetry:)
	curl -sSL https://install.python-poetry.org | $(PYTHON) -
	@PATH="/root/.local/bin:$(PATH)"
	@export PATH
	poetry config virtualenvs.in-project true
	poetry install

docker-build-common:
	cd common && $(DOCKER) build -t $(PROJECT_NAME)_common .

docker-build-data: docker-build-common
	cd data && $(DOCKER) build -t $(PROJECT_NAME)_data .

docker-build-models: docker-build-common
	cd data && $(DOCKER) build -t $(PROJECT_NAME)_datamodels .

docker-build-login: docker-build-common
	cd login && $(DOCKER) build -t $(PROJECT_NAME)_login . 

docker-build-game: docker-build-common
	cd game && $(DOCKER) build -t $(PROJECT_NAME)_game . 

docker-build: docker-build-common docker-build-data docker-build-models docker-build-login docker-build-game

compose-build:
	$(COMPOSE) build

python:
	PYTHONSTARTUP=.pythonrc python

help:
	$(info compose-build)
	$(info docker-build-common)
	$(info docker-build-data)
	$(info docker-build-game)
	$(info docker-build-login)
	$(info docker-build)
	$(info format)
	$(info help)
	$(info install_requirements)
	$(info install)
	$(info lint)
	$(info python)
	$(info test)
	@:
