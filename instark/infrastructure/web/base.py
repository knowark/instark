from flask import Flask
from flask_cors import CORS
from ..config import Context
from .api import create_api
# from .routes import set_routes


def create_app(context: Context):
    config = context.config
    registry = context.registry

    app = Flask(__name__)
    CORS(app)
    app.config['SWAGGER'] = {
        'title': 'Instark'
    }

    api = create_api(app, registry)

    return app
