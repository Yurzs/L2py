FROM l2py_common

WORKDIR /code/datta

ADD data/ /code/data/
ADD pyproject.toml /code/

RUN poetry update --no-interaction --no-ansi
RUN poetry install --no-interaction --no-ansi

CMD ["poetry", "run", "python", "/code/data/runner.py"]
