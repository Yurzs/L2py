
PROJECT_NAME = l2py
PYTHON_VERSION = 3.10
UNAME = $(shell uname)
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
	$(info Installing requirements:)
ifeq ($(UNAME),Darwin)
	brew install openssl; \
	brew install swig; \
	export LDFLAGS="-L$(brew --prefix openssl)/lib" \
	CFLAGS="-I$(brew --prefix openssl)/include" \
	SWIG_FEATURES="-cpperraswarn -includeall -I$(brew --prefix openssl)/include"
endif
ifeq ($(UNAME),Linux)
	$(foreach bin,$(REQUIRED_PACKAGES),\
		$(if $(shell command -v $(bin) 2> /dev/null),\
		$(info $(bin) is installed),\
		$(info $(bin) not found, trying to install); $(shell sudo apt-get install $(bin)\
		)))
endif
	@:

check_requirements:
	$(info Checking requirements:)
	$(foreach bin,$(REQUIRED_PACKAGES),\
    	$(if $(shell command -v $(bin) 2> /dev/null),$(info $(bin) is installed),$(error $(bin) not found, please install)))
	@:


install: install_requirements
	$(info Installing poetry:)
	curl -sSL https://install.python-poetry.org | python3 -
	@PATH="/root/.local/bin:$(PATH)"
	@export PATH
	poetry install
	

docker-build-data:
	docker build -t $(PROJECT_NAME)_data . -f ./data/Dockerfile

docker-build-login:
	docker build -t $(PROJECT_NAME)_login . -f ./login/Dockerfile

docker-build-game:
	docker build -t $(PROJECT_NAME)_game . -f ./game/Dockerfile

docker-build: docker-build-game docker-build-login docker-build-data

compose-build:
	docker-compose build 

python:
	PYTHONSTARTUP=.pythonrc python
