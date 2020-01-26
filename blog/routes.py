from flask import request, jsonify
from flask_api import status

from blog import app
from blog.controller.view import insert, get, update, delete, get_all
from blog.DB.model import UserSchema

user_schema = UserSchema()


@app.route('/', methods=['GET'])
def get_all_user():
    user_list_schema = UserSchema(many=True)
    users = get_all()
    if users:
        return jsonify(user_list_schema.dump(users))
    return jsonify({"OOps! ": "No user Exists"}, status.HTTP_404_NOT_FOUND)


@app.route('/', methods=['POST'])
def insert_user():
    user = insert(**request.json)
    if isinstance(user, dict):
        return jsonify(user, status.HTTP_406_NOT_ACCEPTABLE)
    return jsonify(user_schema.dump(user), status.HTTP_201_CREATED)


@app.route('/<user_id>', methods=['GET'])
def get_user(user_id):
    user = get(user_id)
    if isinstance(user, str):
        return jsonify(user, status.HTTP_404_NOT_FOUND)
    else:
        return jsonify(user_schema.dump(user))


@app.route('/<user_id>', methods=['PUT'])
def update_user(user_id):
    user = update(user_id, **request.json)
    if isinstance(user, dict):
        return jsonify(user, status.HTTP_406_NOT_ACCEPTABLE)
    return jsonify(user_schema.dump(user), status.HTTP_200_OK)


@app.route('/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = delete(user_id)
    if user:
        return jsonify({"User with id {} deleted successfully".format(user_id)}, status.HTTP_202_ACCEPTED)
    return jsonify({"User with id {} does not exists ".format(user_id)}, status.HTTP_200_OK)
