from flask import Flask

from .blueprints import restapi
from .extensions import cors


__version__ = '0.1.0'

def create_app_minimal():
    app = Flask(__name__)

    return app

def create_app():
    app = create_app_minimal()

    restapi.init_app(app)
    cors.init_app(app)

    return app