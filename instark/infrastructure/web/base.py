from flask import Flask
from flask_cors import CORS
from ..config import Context
from .routes import set_routes


def create_app(context: Context):
    app = Flask(__name__)
    CORS(app)

    set_routes(app)

    return app
