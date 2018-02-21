from moonitor import container, client

if __name__ == '__main__':
    c = container.Containers()
    print(c.get_container_attrs())
