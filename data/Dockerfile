FROM l2py_common

ADD data /code/data
ADD requirements.txt /code
ADD setup.py /code

WORKDIR /code
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python setup.py install

CMD ["python", "/code/data/runner.py"]
