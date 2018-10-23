FROM python:3.5.6-slim-stretch
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
ADD VERSION .

ADD ./notification_microservice /code/

RUN pip install --upgrade pip
RUN pip install -r requirements/dev.txt
