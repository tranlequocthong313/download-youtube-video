FROM python:3.7-slim

WORKDIR /app

COPY __init__.py ./

RUN pip install -
