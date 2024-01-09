#!/usr/bin/python3
"""import city_views and creates a route"""

from flask import jsonify, Blueprint, abort, request
from api.v1.views import user_views
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json


@user_views.route("/users", strict_slashes=False, methods=["GET"])
def return_users():
    """returns all state objects"""
    all_users = storage.all(User).values()
    users_list = []
    for user in all_users:
        users_list.append(user.to_dict())
    return jsonify(users_list)


@user_views.route("/users/<user_id>", strict_slashes=False,
                  methods=["GET", "DELETE"])
def return_user_by_id(user_id):
    """Returns state based on city_id"""
    if request.method == "GET":
        all_users = storage.get(User, user_id)
        if not all_users:
            abort(404)
        return jsonify(all_users.to_dict())

    elif request.method == "DELETE":
        user = storage.get(User, user_id)
        if user is None:
            abort(404)

        storage.delete(user)
        storage.save()
        return jsonify({}), 200


@user_views.route("/users", strict_slashes=False,
                  methods=["POST"])
def post_user():
    """posts a new state"""
    if request.method == "POST":
        if not request.get_json():
            abort(400, description="Not a JSON")
        if 'email' not in request.get_json():
            abort(400, description="Missing email")
        if 'password' not in request.get_json():
            abort(400, description="Missing password")

        user_data = request.get_json()
        new_user = User(**user_data)
        new_user.save()
        return jsonify(new_user.to_dict()), 201


@user_views.route("/users/<user_id>", methods=["PUT"])
def update_user(user_id):
    """updates data on a city"""
    if request.method == "PUT":
        all_users = storage.get(User, user_id)
        if not all_users:
            abort(404)
        if not request.get_json():
            abort(400, description="Not a JSON")
        data = request.get_json()
        for key, value in data.items():
            if key not in ["id", "email", "created_at", "updated_at"]:
                setattr(all_users, key, value)

        storage.save()
        return jsonify(all_users.to_dict()), 200
