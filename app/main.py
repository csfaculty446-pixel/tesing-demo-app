from flask import Blueprint, request, jsonify, g, current_app
from .utils import add_numbers, validate_user
from .database import get_db, add_user_if_not_exists


bp = Blueprint('main', __name__)


@bp.route('/', methods=['GET'])
def index():
return jsonify({'message': 'Testing Demo App'}), 200


@bp.route('/add', methods=['GET'])
def add_route():
# expects ?a=2&b=3
a = request.args.get('a', type=int)
b = request.args.get('b', type=int)
if a is None or b is None:
return jsonify({'error': 'a and b query params required'}), 400
return jsonify({'result': add_numbers(a, b)}), 200


@bp.route('/signup', methods=['POST'])
def signup():
data = request.get_json() or {}
username = data.get('username')
password = data.get('password')
if not username or not password:
return jsonify({'error': 'username and password required'}), 400


# simple validation
if not validate_user(username, password):
return jsonify({'error': 'invalid username/password format'}), 400


add_user_if_not_exists(username, password)
return jsonify({'status': 'user created', 'username': username}), 201


@bp.route('/login', methods=['POST'])
def login():
data = request.get_json() or {}
username = data.get('username')
password = data.get('password')
if not username or not password:
return jsonify({'error': 'username and password required'}), 400


db = get_db()
user = db.execute('SELECT id, username FROM users WHERE username = ? AND password = ?', (username, password)).fetchone()
if user:
return jsonify({'status': 'ok', 'username': user['username']}), 200
return jsonify({'status': 'invalid credentials'}), 401
