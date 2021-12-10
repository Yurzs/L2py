FROM l2py-common as l2py-data

WORKDIR /code/
ADD data/pyproject.toml /code/
RUN /root/.local/bin/poetry update && /root/.local/bin/poetry install
CMD ["/root/.local/bin/poetry", "run", "python", "/code/data/runner.py"]