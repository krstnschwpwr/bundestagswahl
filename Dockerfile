FROM ubuntu:latest
MAINTAINER Kristine Schwabauer "schwabauer.kristine@googlemail.com"

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app

ENV LANG C.UTF-8
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["run.py"]