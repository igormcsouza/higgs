from flask import Blueprint
from flask_restful import Api

from backend.blueprints.restapi import resources


bp = Blueprint(__name__, "api", url_prefix="/api")
api = Api(bp)

resources.init_api(api)

def init_app(app):
    app.register_blueprint(bp)
