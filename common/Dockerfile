FROM python:3.10.3

ENV PATH $PATH:/root/.local/bin
ENV PYTHONPATH /code
ENV PYTHONBUFFERED 1

ADD common /code/common/
ADD pyproject.toml /code/
ADD bin/sitecustomize.py /code

WORKDIR /code

RUN pip install --upgrade pip
RUN apt-get update && apt-get install -y build-essential swig

RUN curl -sSL https://install.python-poetry.org | python3 -

RUN poetry config virtualenvs.in-project true
RUN poetry config experimental.new-installer false
RUN poetry install --no-interaction --no-ansi
