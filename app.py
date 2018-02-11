from db.dataAccess import dbAccess
from flask import Flask, render_template, json, request


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/volumes', methods=['GET', 'POST'])
def collection():
    if request.method == 'GET':
        volumes = dbAccess.get_all_volumes_current_value()
        return json.dumps(volumes)
    elif request.method == 'POST':
        dbAccess.publish_data()
        return 'Success'


@app.route('/api/volumes/<string:name>', methods=['GET'])
def collection_name(name):
    volume = dbAccess.get_volume_by_name(name)
    return json.dumps(volume)


if __name__ == '__main__':
    app.run()
