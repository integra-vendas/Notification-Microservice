FROM python:3.5.6-slim-stretch
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
ADD . /code
WORKDIR /code/notification_microservice

RUN pip install --upgrade pip
RUN pip install -r requirements/dev.txt
