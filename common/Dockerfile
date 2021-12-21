FROM python:3.10.0

ADD common /code/common
ADD pyproject.toml /code/
ADD sitecustomize.py /code

RUN apt-get update && apt-get install -y build-essential swig
RUN curl -sSL https://install.python-poetry.org | python -

ENV PATH $PATH:/root/.local/bin

WORKDIR /code/

RUN poetry config virtualenvs.in-project true
RUN poetry install
