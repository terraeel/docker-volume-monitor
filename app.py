import sqlite3

from flask import Flask, render_template, json
app = Flask(__name__)


def get_volumes():
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


@app.route('/api/volumes', methods=['GET'])
def collection():
    volumes = get_volumes()
    return json.dumps(volumes)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':

    app.run()
