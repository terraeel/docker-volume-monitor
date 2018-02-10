
import os
import sys
import docker
import sqlite3
import time


def get_dir_size(client):
    print(client.df()["Volumes"][2]["UsageData"]["Size"])

def publish_data():
    conn = sqlite3.connect('volumes.db')
    c = conn.cursor()
    client = docker.from_env()
    volume = client.volumes.list()
    for volumes in volume:
        name = volumes.name
        mountpoint = volumes.attrs['Mountpoint']
        size = get_dir_size(mountpoint)
        c.execute("INSERT INTO volumes (name, mountpoint, size) VALUES (?,?,?)", (name, mountpoint, size))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    while True:
        publish_data()
        time.sleep(30)

