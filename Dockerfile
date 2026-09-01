# syntax=docker/dockerfile:1
FROM public.ecr.aws/docker/library/python:3.14-slim-trixie
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /src
COPY requirements.txt /src/
RUN apt update
RUN apt install -y npm
RUN pip install --upgrade pip
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    libgssapi-krb5-2 \
    libsasl2-2 \
    && rm -rf /var/lib/apt/lists/*
RUN pip install --no-deps -r requirements.txt
COPY . /src/