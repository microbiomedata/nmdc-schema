FROM python:3.9

ADD . /src/

RUN \
    pip install poetry && \
    cd /src && poetry install 
