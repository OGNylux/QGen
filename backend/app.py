import json
import os

from flask import Flask, send_from_directory, request, jsonify, send_file, after_this_request, current_app
from flask_cors import CORS, cross_origin
import random
from bson import ObjectId
from bson.json_util import dumps
from pymongo import MongoClient

from QuestDataGenerator import QuestDataGenerator

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.json.sort_keys = False

cluster = MongoClient(host="localhost", port=27017, serverSelectionTimeoutMS=1000)

db = cluster.qgen
questLines = db.questlines


# Path for our main Svelte page
@app.route("/")
def base():
    return send_from_directory('client/public', 'index.html')


# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
@cross_origin()
def home(path):
    return send_from_directory('client/public', path)


@app.route("/rand")
def hello():
    test = {"number": random.randint(0, 100)}
    return jsonify(test)


@app.route("/test2", methods=['GET', 'POST'])
def test2():
    data = json.loads(request.data.decode('utf-8'))
    quests = data['quests']

    QuestDataGenerator(quests)

    return data


@app.route("/generator", methods=['POST'])
def generator():

    test = ['const a = "test"', 'npc.dialogue = hallo', '{\n"translate":"entity.pb:hugo.name"\n}', '{\n"translate":"entity.pb:hugo.name"\n}']

    return test


@app.route("/test", methods=['GET'])
def hi():
    file_path = "./test.txt"
    file_handle = open(file_path, 'r')

    # This *replaces* the `remove_file` + @after_this_request code above
    def stream_and_remove_file():
        yield from file_handle
        file_handle.close()
        os.remove(file_path)

    return current_app.response_class(
        stream_and_remove_file(),
        headers={'Content-Disposition': 'attachment', 'filename': 'test.txt'}
    )


@app.route('/db/questlines', methods=['GET', 'POST'])
def groups():
    if request.method == 'GET':
        booking = dumps(list(questLines.find({})))
        return booking

    if request.method == 'POST':
        data = json.loads(request.data.decode('utf-8'))['data']
        npc = data['npc']
        questData = data['questData']
        date = data['date']

        new_obj = {
            'npc': npc,
            'questData': questData,
            'date': date
        }
        questLines.insert_one(new_obj)
        return 'OK', 200


@app.route('/db/questlines/<string:group_id>', methods=['PUT', 'DELETE'])
def single_group(group_id):
    if request.method == 'PUT':
        if len(list(questLines.find({"_id": ObjectId(group_id)}))) > 0:
            data = json.loads(request.data.decode('utf-8'))['data']
            npc = data['npc']
            questData = data['questData']
            date = data['date']

            new_obj = {
                'npc': npc,
                'questData': questData,
                'date': date
            }

            questLines.update_one({"_id": ObjectId(group_id)}, {"$set": new_obj})
            return 'OK', 200
        return 'Nothing Found', 404

    if request.method == 'DELETE':
        if len(list(questLines.find({"_id": ObjectId(group_id)}))) > 0:
            questLines.delete_one({"_id": ObjectId(group_id)})
            return dumps(list(questLines.find({})))
        return 'Nothing Found', 404


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
