FROM python:3.8
ADD loginserver /code/l2pylogin/loginserver
ADD requirements.txt /code/l2pylogin/
ADD setup.py /code/l2pylogin/
WORKDIR /code/l2pylogin/
RUN apt update
RUN apt install -y build-essential python3-dev swig
RUN pip install -r requirements.txt
RUN python setup.py install
ENV PYTHONBUFFERED 1
CMD python loginserver/runner.py
