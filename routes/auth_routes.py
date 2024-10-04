from flask import Blueprint, jsonify, request
from models.user_model import register_user, authenticate_user, get_all_users

auth_blueprint = Blueprint('auth', __name__)

# User registration route
@auth_blueprint.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username and password:  # Check for non-empty fields
        if register_user(username, password):
            return jsonify({'message': 'User registered successfully'}), 201
        else:
            return jsonify({'message': 'Error registering user'}), 500
    else:
        return jsonify({'message': 'Invalid input'}), 400


# User authentication route
@auth_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if authenticate_user(username, password):
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 401

# Get all users route
@auth_blueprint.route('/users', methods=['GET'])
def get_users():
    users = get_all_users()

    # Format the response as a list of user objects
    users_list = [{'id': user[0], 'username': user[1]} for user in users]

    return jsonify(users_list), 200
