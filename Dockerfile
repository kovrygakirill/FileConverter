FROM python:3.10.6-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

WORKDIR /code/

RUN apt-get update && apt-get install -y libreoffice
RUN pip install pipenv

COPY Pipfile Pipfile.lock /code/

RUN pipenv install --system --deploy --ignore-pipfile

COPY . /code/