from flask import Blueprint, request, jsonify
from services.user_service import (
    get_all_users, get_user_by_id, create_user, update_user, delete_user,
    search_users_by_name, login_user
)

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/')
def home():
    return "User Management System"

@user_bp.route('/users', methods=['GET'])
def get_users():
    return get_all_users()

@user_bp.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    return get_user_by_id(user_id)

@user_bp.route('/users', methods=['POST'])
def add_user():
    return create_user(request.json)

@user_bp.route('/user/<user_id>', methods=['PUT'])
def modify_user(user_id):
    return update_user(user_id, request.json)

@user_bp.route('/user/<user_id>', methods=['DELETE'])
def remove_user(user_id):
    return delete_user(user_id)

@user_bp.route('/search', methods=['GET'])
def search_users():
    name = request.args.get('name')
    return search_users_by_name(name)

@user_bp.route('/login', methods=['POST'])
def login():
    return login_user(request.json)
