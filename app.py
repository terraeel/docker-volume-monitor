from db.dataAccess import dbAccess
from flask import Flask, render_template, jsonify, request, json
import requests

app = Flask(__name__, static_folder="./static", template_folder="./templates")


@app.route('/', defaults={'path': ''})
def index(path):
    if app.debug:
        print("Debug")
        return requests.get('http://localhost:8080/{}'.format(path)).text
    return render_template("index.html")


@app.route('/api/volumes', methods=['GET', 'POST'])
def collection():
    if request.method == 'GET':
        volumes = dbAccess.get_all_volumes_current_value()
        return jsonify(volumes)
    elif request.method == 'POST':
        dbAccess.publish_data()
        return 'Success'


@app.route('/api/volumes/<string:name>', methods=['GET'])
def collection_name(name):
    volume = dbAccess.get_volume_by_name(name)
    return json.dumps(volume)


if __name__ == '__main__':
    app.run(host='localhost', threaded=True, port=5000)
