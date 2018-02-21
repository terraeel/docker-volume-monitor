from moonitor import client


class Containers:

    def __init__(self):
        c = client.Client()
        self.containers = c.get_containers()

    def get_container_attrs(self):
        containersdict = {}
        for c in self.containers:
            i = self.get_container_id(c)
            containersdict[i] = [{'Name': self.get_container_names(c)}]
            containersdict[i].append({'Status': self.get_container_status(c)})
            containersdict[i].append({'Logs': self.get_container_output(c)})
        return containersdict

    def get_container_status(self, c):
        try:
            return c.attrs['State']['Health']['Status']
        except KeyError:
            return c.attrs['State']['Status']

    def get_container_output(self, c):
        try:
            return c.attrs['State']['Health']['Log'][0]['Output']
        except KeyError:
            return

    def get_container_names(self, c):
        name = c.attrs['Name'][1:]
        return name

    def get_container_id(self, c):
        id = c.attrs['Id'][0:10]
        return id
