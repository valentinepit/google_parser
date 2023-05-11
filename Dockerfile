FROM python:3.8 as builder

RUN mkdir app
WORKDIR app

RUN pip install --upgrade pip

COPY app/requirements.txt .
RUN pip install -r requirements.txt

COPY app .


