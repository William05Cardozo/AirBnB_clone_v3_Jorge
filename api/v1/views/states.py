#!/usr/bin/python3
"""
Create a new view for State objects that handles
all default RESTFul API actions
"""

from models import storage
from models.state import State
from api.v1.views import app_views
from flask import Flask, Blueprint, jsonify, abort

@app_views.route("/states", methods=['GET'], strict_slashes=False)
@app_views.route("/states/<states_id", methods=['GET'], strict_slashes=False)
def my_state(state_id=None):
    list_state = []
    if state_id == None:
        for value in storage.all ("State").value():
            list_state.append(value.to_dict())
        return jsonify(list_state)
    else:
        state = storage.get("State", state_id)
        if state == None:
            abort(404)
        return jsonify(state.to_dict())
