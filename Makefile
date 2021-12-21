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
	$(DOCKER) build -t $(PROJECT_NAME)_common . -f ./common/Dockerfile

docker-build-data:
	$(DOCKER) build -t $(PROJECT_NAME)_data . -f ./data/Dockerfile

docker-build-login:
	$(DOCKER) build -t $(PROJECT_NAME)_login . -f ./login/Dockerfile

docker-build-game:
	$(DOCKER) build -t $(PROJECT_NAME)_game . -f ./game/Dockerfile

docker-build: docker-build-common docker-build-data docker-build-login docker-build-game

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
