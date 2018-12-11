import docker 
client = docker.from_env()

print client.services.create("nclcloudcomputing/javabenchmarkapp", name='primecheck', mode={'Replicated': {'Replicas': 2}}, endpoint_spec= docker.types.EndpointSpec(mode='vip', ports={80:8080}))
print client.services.create("bitnami/mongodb:latest", name='mongo', endpoint_spec= docker.types.EndpointSpec(mode='vip', ports={3306:27017}))
print client.services.create("dockersamples/visualizer", name="visualiser", mounts=['/var/run/docker.sock:/var/run/docker.sock:rw'], endpoint_spec= docker.types.EndpointSpec(mode='vip', ports={88:8080}))
print client.services.create("google/cadvisor", name="monitor", mounts=['/:/rootfs:ro', '/var/run:/var/run:ro', '/sys:/sys:ro', '/var/lib/docker:/var/lib/docker:ro', '/dev/disk:/dev/disk:ro'], endpoint_spec= docker.types.EndpointSpec(mode='vip', ports={4000:8080}))