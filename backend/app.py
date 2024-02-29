import json

from flask import Flask, send_from_directory, request, jsonify
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


@app.route('/db/questlines', methods=['GET', 'POST'])
def groups():
    if request.method == 'GET':
        booking = dumps(list(questLines.find({})))
        return booking

    if request.method == 'POST':
        data = json.loads(request.data.decode('utf-8'))['data']
        npc = data['npc']
        quests = data['quests']
        date = data['date']

        new_obj = {
            'npc': npc,
            'questData': quests,
            'date': date
        }
        questLines.insert_one(new_obj)
        return 'OK', 200


@app.route('/db/questlines/<string:group_id>', methods=['PUT', 'DELETE'])
def single_group(group_id):
    if request.method == 'PUT':
        pass

    if request.method == 'DELETE':
        if len(list(questLines.find({"_id": ObjectId(group_id)}))) > 0:
            questLines.delete_one({"_id": ObjectId(group_id)})
            return dumps(list(questLines.find({})))
        return 'Nothing Found', 404


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
