FROM l2py_datamodels

ADD login /code/login
ADD pyproject.toml /code/

WORKDIR /code/

RUN poetry update && poetry install

CMD ["poetry", "run", "python", "/code/login/runner.py"]
