FROM l2py-common as l2py-game

WORKDIR /code/
ADD game/game /code/game
ADD game/pyproject.toml /code/
RUN /root/.local/bin/poetry update && /root/.local/bin/poetry install
CMD ["/root/.local/bin/poetry", "run", "python", "/code/game/runner.py"]