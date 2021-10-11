FROM python:3.10

ENV PYTHONBUFFERED 1

RUN mkdir "/code"
ADD common /code/common
ADD requirements.txt /code
ADD setup.py /code

RUN apt update
RUN apt install -y build-essential

WORKDIR /code
RUN pip install --upgrade pip wheel
RUN pip install -r requirements.txt
RUN python setup.py install --single-version-externally-managed --root=/
RUN rm -rf /code
