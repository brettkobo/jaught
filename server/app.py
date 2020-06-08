import helper
import json
from flask import Flask, request, Response, jsonify
from flask_cors import CORS
from data_models import db, Journal, User
import jwt
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config.from_object(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///journey.db'
app.config['SECRET_KEY'] = "random string"

db.init_app(app)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

def token_required(f):
    @wraps(f)
    def _verify(*args, **kwargs):
        auth_headers = request.headers.get('Authorization', '').split()

        invalid_msg = {
            'message': 'Invalid token. Registeration and / or authentication required',
            'authenticated': False
        }
        expired_msg = {
            'message': 'Expired token. Reauthentication required.',
            'authenticated': False
        }

        if len(auth_headers) != 2:
            return jsonify(invalid_msg), 401

        try:
            token = auth_headers[1]
            data = jwt.decode(token, current_app.config['SECRET_KEY'])
            user = User.query.filter_by(email=data['sub']).first()
            if not user:
                raise RuntimeError('User not found')
            return f(user, *args, **kwargs)
        except jwt.ExpiredSignatureError:
            return jsonify(expired_msg), 401 # 401 is Unauthorized HTTP status code
        except (jwt.InvalidTokenError, Exception) as e:
            print(e)
            return jsonify(invalid_msg), 401

    return _verify


@api.route('/register/', methods=('POST',))
def register():
    data = request.get_json()
    user = User(**data)
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict()), 201


@api.route('/login/', methods=('POST',))
def login():
    data = request.get_json()
    user = User.authenticate(**data)

    if not user:
        return jsonify({ 'message': 'Invalid credentials', 'authenticated': False }), 401

    token = jwt.encode({
        'sub': user.email,
        'iat':datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(minutes=30)},
        current_app.config['SECRET_KEY'])
    return jsonify({ 'token': token.decode('UTF-8') })


@app.route('/pixel/new', methods=('POST',))
def create_pixel():
    data = request.get_json()

    pixel = Journal(note=data['note'],
                    color=data['color'])

    db.session.add(pixel)
    db.session.commit()
    return jsonify(pixel.to_dict())

@app.route('/pixel/', methods=('GET',))
def fetch_pixel():
    journal = Journal.query.all()
    return jsonify([s.to_dict() for s in journal])


# ----------------


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
    color = note_data['color']

    print(note_data)
    # Add item to the list
    note_data = helper.add_to_notes(title, body, tags, color)

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
