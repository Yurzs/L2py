FROM python:3.10

COPY entrypoint.sh /entrypoint.sh
COPY . /app/

RUN chmod +x /entrypoint.sh
RUN apt-get update && apt-get install swig openssl
RUN pip install black isort pylint
ENTRYPOINT [ "/entrypoint.sh" ]