from flask import Blueprint, jsonify


bp = Blueprint(__name__, "health", url_prefix="/health")

@bp.route("/")
def health():
    return jsonify({ "health": True })

def init_app(app):
    app.register_blueprint(bp)
