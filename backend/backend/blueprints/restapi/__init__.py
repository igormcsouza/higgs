from flask import Blueprint
from flask_restful import Api


bp = Blueprint(__name__, "api", url_prefix="/api")
api = Api(bp)

def init_app(app):
    app.register_blueprint(bp)
