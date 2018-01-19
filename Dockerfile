FROM ubuntu:latest
MAINTAINER Kristine Schwabauer "schwabauer.kristine@googlemail.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential wget

COPY . /app
ENV HOME=/app
WORKDIR = /app

#install python web server and dependencies
COPY requirements.txt /tmp
WORKDIR /tmp
RUN pip install -r requirements.txt


#expose port
EXPOSE 8080

ENTRYPOINT ["python", "0.0.0.0:8080", "run:app"]

