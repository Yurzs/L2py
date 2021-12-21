FROM l2py_common

ADD data /code/data
ADD pyproject.toml /code/

WORKDIR /code/

RUN poetry update && poetry install

CMD ["poetry", "run", "python", "/code/data/runner.py"]
