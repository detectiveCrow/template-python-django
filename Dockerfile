FROM python:3.8.10

MAINTAINER HOSEONG LEE <detectivecrow2540@gmail.com>

WORKDIR /usr/src/app

COPY ./requirements.txt /usr/src/app
RUN pip3 install -r ./requirements.txt

COPY . /usr/src/app
