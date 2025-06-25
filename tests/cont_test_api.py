import docker

client = docker.from_env()

# docker build -t <name> -f <tests/Dockerfile> .
client.images.build(path = '.', dockerfile = 'tests/Dockerfile', tag = 'run_api_tests')

# docker run run_api_tests
print(client.containers.run('run_api_tests'))