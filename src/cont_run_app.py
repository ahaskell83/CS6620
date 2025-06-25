import docker

client = docker.from_env()

# docker build -t <name> -f <tests/Dockerfile> .
client.images.build(path = '.', dockerfile = 'src/Dockerfile', tag = 'run_app')
print('past build')
# docker run run_api_tests
print(client.containers.run('run_app', command= ["sh", "-c", "python src/cat_pkg/assign_2.py"],ports={'5000/tcp': 5000}))

print('past run')