
PROJECT_NAME = l2py
PYTHON_VERSION = 3.10
UNAME = $(shell uname)

lint:
	black --check .
	isort -c --profile=black .

format:
	black .
	isort --profile=black .


test:
	pytest .

create_venv:
	python$(PYTHON_VERSION) -m venv .venv

activate:
	. .venv/bin/activate; \
	bin/activate


venv: create_venv activate install_requirements

install_lint:
	pip install black isort


install_requirements:
ifeq ($(UNAME),Darwin)
	brew install openssl; \
	brew install swig; \
	export LDFLAGS="-L$(brew --prefix openssl)/lib" \
	CFLAGS="-I$(brew --prefix openssl)/include" \
	SWIG_FEATURES="-cpperraswarn -includeall -I$(brew --prefix openssl)/include"
endif

	for module in common data game login ; do \
		cd $$module; \
		pip install -r requirements.txt; \
		cd ..; \
	done

install: install_requirements install_lint

docker-build-common:
	cd common && docker build -t $(PROJECT_NAME)_common .

docker-build-data-models: docker-build-common
	cd data && docker build -f models.Dockerfile -t $(PROJECT_NAME)_data_models .

docker-build-data: docker-build-common
	cd data && docker build -t $(PROJECT_NAME)_data .

docker-build-login: docker-build-data-models
	cd login && docker build -t $(PROJECT_NAME)_login .

docker-build-game: docker-build-data-models
	cd game && docker build -t $(PROJECT_NAME)_game .


docker-build: docker-build-game docker-build-login docker-build-data

compose-build: docker-build-data-models
	docker-compose build

python:
	PYTHONSTARTUP=.pythonrc python
