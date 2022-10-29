FROM python:3.10-bullseye
ENV PYTHONUNBUFFERED 1
ENV IS_RUNNING_IN_CONTAINER Yes
RUN mkdir /code
RUN apt-get update && \
    apt-get install -y git build-essential cmake clang libssl-dev
COPY requirements.txt /code/requirements.txt
WORKDIR /code
RUN pip install -r requirements.txt
ADD . /code/
COPY . /code
