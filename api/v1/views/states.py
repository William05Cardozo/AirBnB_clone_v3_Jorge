#!/usr/bin/python3
"""index from views"""

from api.v1.views import app_views
from flask import Flask, Blueprint, jsonify, abort
from models import storage


@app_views.route('/states', methods=['GET'], strict_slashes=False)
@app_views.route('/states/<state_id>', methods=['GET'],
                 strict_slashes=False)
def get_states(state_id=None):
    list_states = []
    if state_id is None:
        for val_state in storage.all("State").values():
            list_states.append(val_state.to_dict())
        return jsonify(list_states)
    else:
        state = storage.get("State", state_id)
        if state != None:
            return jsonify(state.to_dict())
        else:
            abort(404)

@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_states(state_id=None):
    state = storage.get("State", state_id)
    if state != None:
        storage.delete(state)
        return jsonify({}), 200
    else:
        abort(404)
