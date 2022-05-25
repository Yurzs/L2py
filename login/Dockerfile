FROM l2py_common

WORKDIR /code/

ADD login /code/login
ADD pyproject.toml /code/

COPY bin/ /usr/local/bin/
RUN chmod +x -R /usr/local/bin

RUN poetry update --no-interaction --no-ansi
RUN poetry install --no-interaction --no-ansi

CMD ["poetry", "run", "python", "/code/login/runner.py"]
