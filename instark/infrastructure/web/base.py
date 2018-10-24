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
    # app.config.SWAGGER_UI_DOC_EXPANSION = 'full'

    api = create_api(app, registry)

    api.init_app(app)

    # set_routes(app, registry)

    return app
