from flask import Flask, jsonify

from .blueprints import restapi, health
from .extensions import cors


__version__ = '0.1.0'

def create_app_minimal():
    app = Flask(__name__)

    return app

def create_app():
    app = create_app_minimal()

    @app.route("/")
    def main():
        return jsonify({
            "health": "/health",
            "docs": "..."
        })

    # Blueprints
    restapi.init_app(app)
    health.init_app(app)

    # Extensions
    cors.init_app(app)

    return app