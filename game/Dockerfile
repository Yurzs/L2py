FROM l2py_common

WORKDIR /code/
ADD game /code/game
ADD pyproject.toml /code/

RUN poetry update --no-interaction --no-ansi
RUN poetry install --no-interaction --no-ansi

CMD ["poetry", "run", "python", "./game/runner.py"]
