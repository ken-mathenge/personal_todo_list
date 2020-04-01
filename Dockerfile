FROM python:3.6

#Set up environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

#working directory
WORKDIR /code

#Install dependancies
COPY requirements.txt /code
RUN pip3 install -rrequirements.txt

#Copy changes over
COPY . /code