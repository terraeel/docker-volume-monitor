import sqlite3
import data
import database
from flask import Flask, render_template, json


app = Flask(__name__)


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


@app.route('/api/volumes/all', methods=['GET'])
def collection():

    volumes = get_all_volumes()
    return json.dumps(volumes)


@app.route('/api/volumes/<string:name>', methods=['GET'])
def collection_name(name):

    volume = get_volume_by_name(name)
    return json.dumps(volume)


@app.route('/api/volumes/delete', methods=['POST'])
def delete():

    database.drop_table()
    database.create_db()
    return True


@app.route('/')
def index():

    return render_template('index.html')


if __name__ == '__main__':

    app.run()
