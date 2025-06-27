#!/bin/bash

docker build -t "run_api_tests" -f "tests/Dockerfile" .

docker run --name "run_tests" "run_api_tests"

docker stop run_tests

