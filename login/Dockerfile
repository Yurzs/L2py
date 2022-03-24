FROM l2py_data

WORKDIR /code/


ADD login /code/login
ADD pyproject.toml /code/

RUN poetry update --no-interaction --no-ansi
RUN poetry install --no-interaction --no-ansi

CMD ["poetry", "run", "python", "/code/login/runner.py"]
