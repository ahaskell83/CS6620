#!/bin/bash


docker build -t "run_app" -f "src/Dockerfile" .

docker run -p "3000:3000" "run_app" 

