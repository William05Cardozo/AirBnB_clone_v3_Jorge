#!/usr/bin/python3
"""__init__ from views"""

from flask import Blueprint

<<<<<<< HEAD
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
=======
from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.amenities import *
>>>>>>> f2277da912bb588292be38fbb65d804a749907ca
from api.v1.views.users import *
from api.v1.views.reviews import *
from api.v1.views.cities import *
from api.v1.views.amenities import *
from api.v1.views.users import *
from api.v1.views.places import *
<<<<<<< HEAD
from api.v1.views.places_reviews import *
=======
>>>>>>> f2277da912bb588292be38fbb65d804a749907ca
