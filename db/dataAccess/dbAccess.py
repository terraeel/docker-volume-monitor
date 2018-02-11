import sqlite3
import docker
import time


def get_all_volumes():

    # publish_data()
    with sqlite3.connect('volumes.db') as connection:
        cursor = connection.cursor()
        cursor.execute('''
            select v.id, v.DATETIME, v.name, v.size
            from volumes v
            inner join (
                select name, max(id) as MaxId
                from volumes
                group by name
            ) vm on v.name = vm.name and v.id = vm.MaxId''')
        all_volumes = cursor.fetchall()
        return all_volumes


def get_volume_by_name(volume_name):

    # publish_data()
    with sqlite3.connect('volumes.db') as connection:
        cursor = connection.cursor()
        cursor.execute('''select * from volumes WHERE name = ? ORDER BY DATETIME''', (volume_name,))
        all_volumes = cursor.fetchall()
        return all_volumes


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
