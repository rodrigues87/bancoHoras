# pull official base image
FROM python:3.8.0-alpine

# set work directory
WORKDIR /Users/aepedro.rodrigues/PycharmProjects/bancoHoras

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /Users/aepedro.rodrigues/PycharmProjects/bancoHoras/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY bancoHoras /Users/aepedro.rodrigues/PycharmProjects/bancoHoras/
