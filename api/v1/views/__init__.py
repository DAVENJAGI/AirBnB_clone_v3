#!/usr/bin/python3
"""imports Blueprint from flask"""

from flask import Blueprint
# from api.v1.views.iindex import *

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")
state_views = Blueprint("state_views", __name__, url_prefix="/api/v1")
city_views = Blueprint("city_views", __name__, url_prefix="/api/v1")
amenity_views = Blueprint("amenity_views", __name__, url_prefix="/api/v1")
user_views = Blueprint("user_views", __name__, url_prefix="/api/v1")

from views.index import *
from views.states import *
from views.cities import *
from views.amenities import *
from views.users import *
