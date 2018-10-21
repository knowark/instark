from flask import Flask
from flask_cors import CORS
from .routes import set_routes


def create_app():
    app = Flask(__name__)
    CORS(app)

    set_routes(app)

    return app
