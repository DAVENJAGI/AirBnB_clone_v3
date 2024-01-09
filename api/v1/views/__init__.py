#!/usr/bin/python3
"""imports Blueprint from flask"""

from flask import Blueprint
# from api.v1.views.iindex import *

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")
state_views = Blueprint("state_views", __name__, url_prefix="/api/v1")
city_views = Blueprint("city_views", __name__, url_prefix="/api/v1")
amenity_views = Blueprint("amenity_views", __name__, url_prefix="/api/v1")
from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.cities import *
from api.v1.views.amenities import *
