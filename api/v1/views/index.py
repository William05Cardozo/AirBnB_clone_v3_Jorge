#!/usr/bin/python3
"""index from views"""

from api.v1.views import app_views
from flask import Flask, Blueprint, jsonify
from models import storage


@app_views.route("/status", strict_slashes=False)
def status():
    """status"""
    return jsonify({"status": "OK"})


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
