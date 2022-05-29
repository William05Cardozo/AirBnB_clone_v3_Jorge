#!/usr/bin/python3
"""
Create a new view for Amenity objects that handles
all default RESTFul API actions
"""

from api.v1.views import app_views
from flask import Flask, Blueprint, jsonify, abort, request
from models import storage
<<<<<<< HEAD
<<<<<<< HEAD
from models.amenities import Amenity
=======
from models.amenity import Amenity
>>>>>>> 35aa7e0baab7d2187afc4013bf18cb87cf5f184b
=======
from models.amenity import Amenity
>>>>>>> storage_get_count


@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
@app_views.route('/amenities/<amenity_id>', methods=['GET'],
                 strict_slashes=False)
def get_amenities(amenity_id=None):
    """get method amenities"""

    list_amt = []
    if amenity_id is None:
        for val_amt in storage.all("Amenity").values():
            list_amt.append(val_amt.to_dict())
        return jsonify(list_amt), 200
    else:
<<<<<<< HEAD
<<<<<<< HEAD
        amenit = storage.get("Amenity", amenity_id)
        if amenit is not None:
=======
        amenity = storage.get("Amenity", amenity_id)
        if amenity is not None:
>>>>>>> 35aa7e0baab7d2187afc4013bf18cb87cf5f184b
=======
        amenity = storage.get("Amenity", amenity_id)
        if amenity is not None:
>>>>>>> storage_get_count
            return jsonify(amenity.to_dict())
        else:
            abort(404)


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_amenities(amenity_id=None):
    """delete method amenities"""

    ament = storage.get("Amenity", amenity_id)
<<<<<<< HEAD
    if ament is not None:
<<<<<<< HEAD
        storage.delete(amenity)
=======
=======
<<<<<<< HEAD
    if amenity is not None:
        storage.delete(amenity)
=======
    if ament is not None:
>>>>>>> storage_get_count
        storage.delete(ament)
>>>>>>> 35aa7e0baab7d2187afc4013bf18cb87cf5f184b
        storage.save()
        return jsonify({}), 200
    else:
        abort(404)


@app_views.route('/amenities', methods=['POST'],
                 strict_slashes=False)
def post_amenities():
    """post method amenities"""
    json_data = request.get_json()
    if not json_data:
        return jsonify({'error': 'Not a JSON'}), 400
    if "name" not in json_data.keys():
        return jsonify({'error': "Missing name"}), 400
    ament = Amenity(**json_data)
<<<<<<< HEAD
    storage.new(amenity)
    storage.save()
    return jsonify(amenity.to_dict()), 201
=======
    storage.save()
    return jsonify(ament.to_dict()), 201
>>>>>>> 35aa7e0baab7d2187afc4013bf18cb87cf5f184b


@app_views.route('/amenities/<amenity_id>', methods=['PUT'],
                 strict_slashes=False)
def put_amenities(amenity_id=None):
    p_amenity = storage.get("Amenity", amenity_id)
    if p_amenity is None:
        abort(404)
    json_data = request.get_json()
    if not json_data:
        return jsonify({'error': 'Not a JSON'}), 400
    for key, value in json_data.items():
        if key != "__class__":
            setattr(p_amenity, key, value)
    storage.save()
    return jsonify(p_amenity.to_dict()), 200
