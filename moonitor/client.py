import docker


class Client:

    def __init__(self):
        self.client = docker.from_env()

    def get_containers(self):
        c = self.client.containers.list()
        return c

    def get_volumes(self, name):
        c = self.client.containers.get(name)
        return c.attrs['Id']
