#!/usr/bin/python3
"""__init__ from views"""

from flask import Blueprint
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')


from api.v1.views.index import *
from api.v1.views.states import *
<<<<<<< HEAD
from api.v1.views.amenities import *
from api.v1.views.users import *
from api.v1.views.reviews import *
=======
from api.v1.views.cities import *
from api.v1.views.amenities import *
from api.v1.views.users import *
from api.v1.views.places import *
>>>>>>> 35aa7e0baab7d2187afc4013bf18cb87cf5f184b
