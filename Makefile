
PROJECT_NAME = l2py
PYTHON_VERSION = 3.10
UNAME = $(shell uname)

format-check:
	black --check .
	isort -c .

format:
	black .
	isort .



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

docker-build-login: docker-build-common
	cd login && docker build -t $(PROJECT_NAME)_login .

docker-build-game: docker-build-common
	cd game && docker build -t $(PROJECT_NAME)_game .

docker-build: docker-build-game docker-build-login

compose-build: docker-build-common
	docker-compose build

python:
	PYTHONSTARTUP=.pythonrc python
