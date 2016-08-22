#!/usr/bin/env bash

tag=$1

echo "Run new docker container"
docker ps -a | grep -P 'dsd$' | awk '{print$1}' | xargs -I {} docker rm -f {} || true
docker run -p 80:80 -p 8000:8000 --name=dsd-${tag} -d chaimozdsd/dsd:${tag}

echo "login container and run function tests"
docker exec dsd bash ./go ft

echo "Remove old docker container"
docker ps -a | grep -P 'dsd$' | awk '{print$1}' | xargs -I {} docker rm -f {} || true
