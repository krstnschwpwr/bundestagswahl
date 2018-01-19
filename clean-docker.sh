#!/usr/bin/env bash

docker stop flaskapp
docker rm flaskapp
docker rmi -f bundestagswahl