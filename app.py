import sqlite3

from flask import Flask, render_template, json
from volum import Volum
app = Flask(__name__)


def get_volumes():
    with sqlite3.connect('volumes.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM volumes")
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
