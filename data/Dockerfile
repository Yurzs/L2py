FROM l2py_common

ADD data /code
ADD requirements.txt /code
ADD setup_models.py /code

WORKDIR /code
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "/code/data/runner.py"]
