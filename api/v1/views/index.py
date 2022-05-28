#!/usr/bin/python3
"""index from views"""

from models import *
from models import storage
from api.v1.views import app_views
from flask import Flask, Blueprint, jsonify
from models import storage


@app_views.route("/status", strict_slashes=False)
def status():
    """status"""
    return jsonify({"status": "OK"})

<<<<<<< HEAD
@app_views.route("/stats", strict_slashes=False)
def stats():
    dictt = {
            "amenities": storage.count(storage.classes['Amenities']),
            "cities": storage.count(storage.classes['City']),
            "places": storage.count(storage.classes['Place']),
            "revies": storage.count(storage.classes['Review']),
            "states": storage.count(storage.classes['State']),
            "users": storage.count(storage.classes['User'])
            }
    return jsonify(dictt)
=======

@app_views.route('/stats', strict_slashes=False)
def stats():
    """methode stats"""
    dictionary = {"amenities": storage.count('Amenity'),
                  "cities": storage.count('City'),
                  "places": storage.count('Place'),
                  "reviews": storage.count('Review'),
                  "states": storage.count('State'),
                  "users": storage.count('User')}
    return jsonify(dictionary)
>>>>>>> 46d82190873ca8fdba30b122e353b837706dd7ce
