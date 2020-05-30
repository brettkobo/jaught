import helper
import json
import uuid
from flask import Flask, request, Response, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/')
def hello_world():
    return 'Hello World!'


# curl -X POST http://127.0.0.1:5000/note/new -d '{"title": "cool note mna", "body": "this is the final countdown", "tags": "final,countdown"}' -H 'Content-Type: application/json'

@app.route('/note/new', methods=['POST'])
def add_note():
    note_data = request.get_json()

    title = note_data['title']
    body = note_data['body']
    tags = note_data['tags']

    print(note_data)
    # Add item to the list
    note_data = helper.add_to_notes(title, body, tags)

    if note_data is None:
        response = Response("{'error': 'note not added - " + title + "'}", status=400, mimetype='application/json')
        return response

    # Return response
    response = Response(json.dumps(note_data), mimetype='application/json')

    return response


@app.route('/note/<noteId>', methods=['DELETE'])
def single_note(noteId):
    res_data = helper.remove_note(noteId);

    # Return response
    response = Response(json.dumps(res_data), mimetype='application/json')
    return response


@app.route('/note/all')
def get_all_items():
    # Get items from the helper
    res_data = helper.get_all_notes()

    # Return response
    response = Response(json.dumps(res_data), mimetype='application/json')
    return response


@app.route('/item/new', methods=['POST'])
def add_item():
    # Get item from the POST body
    req_data = request.get_json()
    item = req_data['item']

    # Add item to the list
    res_data = helper.add_to_list(item)

    # Return error if item not added
    if res_data is None:
        response = Response("{'error': 'Item not added - " + item + "'}", status=400, mimetype='application/json')
        return response

    # Return response
    response = Response(json.dumps(res_data), mimetype='application/json')

    return response


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


if __name__ == '__main__':
    app.run()
