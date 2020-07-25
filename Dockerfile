FROM python:3.7-buster

MAINTAINER onsentamago "tamago4329@gmail.com"

WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app

