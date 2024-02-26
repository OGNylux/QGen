import json

from flask import Flask, send_from_directory, request, jsonify
from flask_cors import CORS, cross_origin
import random

from QuestDataGenerator import QuestDataGenerator

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


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


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
