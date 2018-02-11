import docker
import sqlite3
import time


def publish_data():

    conn = sqlite3.connect('volumes.db')
    c = conn.cursor()
    client = docker.from_env()
    volumes = client.df()["Volumes"]
    for volume in volumes:
        name = volume["Name"]
        size = volume["UsageData"]["Size"]
        c.execute("INSERT INTO volumes (name, size) VALUES (?,?)", (name, size))
    conn.commit()
    conn.close()


if __name__ == '__main__':

    while True:
        publish_data()
        time.sleep(30)

