FROM python:3.10.0

ADD game/game /code/game
ADD common /code/common
ADD data /code/data
ADD game/pyproject.toml /code/
ADD sitecustomize.py /code

WORKDIR /code/
RUN apt-get update
RUN apt-get install -y build-essential swig
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"
RUN export PATH
RUN poetry install

CMD ["poetry", "run", "python", "/code/game/runner.py"]
