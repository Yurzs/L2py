FROM l2py_data_models

ADD login /code/login
ADD requirements.txt /code
ADD setup.py /code

WORKDIR /code
RUN apt install -y build-essential swig
RUN pip install --upgrade pip
RUN python setup.py install

CMD ["python", "/code/login/runner.py"]
