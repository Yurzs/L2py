FROM l2py_data_models

ADD game /code/game
ADD requirements.txt /code
ADD setup.py /code

WORKDIR /code
RUN apt install -y build-essential swig
RUN pip install --upgrade pip wheel
RUN python setup.py install

CMD ["python", "/code/game/runner.py"]
