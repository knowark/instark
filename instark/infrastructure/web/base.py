from flask import Flask
from flask_cors import CORS
from ..config import Context
from .routes import set_routes


def create_app(context: Context):
    config = context.config
    registry = context.registry

    app = Flask(__name__)
    CORS(app)

    set_routes(app, registry)

    return app
