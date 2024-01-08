#!/usr/bin/python3
"""imports app_views and creates a route /status"""

from flask import jsonify, Blueprint, abort, request
from api.v1.views import state_views
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json

# state_views = Blueprint("states", __name__)


@state_views.route("/states", strict_slashes=False)
def return_states():
    """returns all state objects"""
    if request.method == "GET":
        all_states = storage.all(State).values()
        states_list = []
        for state in all_states:
            states_list.append(state.to_dict())
        return jsonify(states_list)


@state_views.route("/states/<state_id>", strict_slashes=False)
def return_state(state_id):
    """Returns state based on state_id"""
    if request.method == "GET":
        all_states = storage.get(State, state_id)
        if not all_states:
            abort(404)
        return jsonify(all_states.to_dict())

    elif request.method == "DELETE":
        all_states = storage.get(State, state_id)
        if all_states is None:
            abort(404)
        storage.delete(all_states)
        return jsonify({}), 200
