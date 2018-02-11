from dataAccess import dbAccess
from flask import Flask, render_template, json


app = Flask(__name__)


@app.route('/api/volumes', methods=['GET'])
def collection():

    volumes = dbAccess.get_all_volumes()
    return json.dumps(volumes)


@app.route('/api/volumes/<string:name>', methods=['GET'])
def collection_name(name):

    volume = dbAccess.get_volume_by_name(name)
    return json.dumps(volume)


@app.route('/')
def index():

    return render_template('index.html')


if __name__ == '__main__':

    app.run()
