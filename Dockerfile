FROM python:3.7-buster

MAINTAINER onsentamago "tamago4329@gmail.com"

RUN pip install --upgrade pip

WORKDIR /code

COPY . .

