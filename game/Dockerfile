FROM l2py_data_models

ADD game /code
ADD requirements.txt /code

WORKDIR /code
RUN apt install -y build-essential swig
RUN pip install --upgrade pip wheel

CMD ["python", "/code/game/runner.py"]
