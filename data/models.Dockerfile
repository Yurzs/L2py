FROM l2py_common

ADD data/__init__.py /code/data/__init__.py
ADD data/models /code/data/models
ADD requirements.txt /code
ADD setup_models.py /code

WORKDIR /code
RUN pip install --upgrade pip wheel
RUN pip install -r requirements.txt
RUN python setup_models.py install --single-version-externally-managed --root=/
RUN rm -rf /code
