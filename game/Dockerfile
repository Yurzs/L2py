FROM l2py_datamodels

ADD game /code/game
ADD pyproject.toml /code/

WORKDIR /code/

RUN poetry update && poetry install

CMD ["poetry", "run", "python", "/code/game/runner.py"]
