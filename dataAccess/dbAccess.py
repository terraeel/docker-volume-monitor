from db import data
import sqlite3


def get_all_volumes():

    data.publish_data()
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

    data.publish_data()
    with sqlite3.connect('volumes.db') as connection:
        cursor = connection.cursor()
        cursor.execute('''select * from volumes WHERE name = ? ORDER BY DATETIME''', (volume_name,))
        all_volumes = cursor.fetchall()
        return all_volumes

