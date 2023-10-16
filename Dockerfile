FROM python:3.11-alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir django_task
WORKDIR  /django_task
COPY ./pyproject.toml ./
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install
COPY . .
