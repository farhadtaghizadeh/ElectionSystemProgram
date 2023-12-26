# syntax=docker/dockerfile:1
# base image
FROM python:3.10

EXPOSE 5000

WORKDIR /python-docker

# pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /python-docker

CMD python app.py