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
    """methode stats

    dictionary = {"amenities": storage.count(storage.classes['Amenity']),
                  "cities": storage.count(storage.classes['City']),
                  "places": storage.count(storage.classes['Place']),
                  "reviews": storage.count(storage.classes['Review']),
                  "states": storage.count(storage.classes['State']),
                  "users": storage.count(storage.classes['User'])}"""
    return jsonify(storage.classes['Amenity'])
