import docker

client = docker.from_env()


client.images.build(path = '.', dockerfile = 'src/Dockerfile', tag = 'run_app')


#print(client.containers.run('run_app', command= ["sh", "-c", "python src/cat_pkg/assign_2.py"],ports={'5000/tcp': 5000}))
cont = client.containers.run('run_app',detach=False,ports={3000:3000})

print(cont)