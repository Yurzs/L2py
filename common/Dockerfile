FROM python:3.10.0 as l2py-common


ADD common/common /code/common
ADD common/pyproject.toml /code/
ADD data/data /code/data
ADD sitecustomize.py /code

RUN apt-get update && apt-get install -y build-essential swig
RUN curl -sSL https://install.python-poetry.org | python3 -
WORKDIR /code/
RUN /root/.local/bin/poetry install
CMD ["true"]