FROM l2py-common as l2py-login

WORKDIR /code/
ADD login/login /code/login
ADD login/pyproject.toml /code/
RUN /root/.local/bin/poetry update && /root/.local/bin/poetry install
CMD ["/root/.local/bin/poetry", "run", "python", "/code/login/runner.py"]