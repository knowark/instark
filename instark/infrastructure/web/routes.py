from flask import Flask
from flask_restful import Api
from .resources import DeviceResource


def set_routes(app: Flask) -> None:

    @app.route('/')
    def index() -> str:
        return "Welcome to Instark!"

    # Restful API
    api = Api(app)
   
    # Devices Resource
    api.add_resource(DeviceResource, '/devices', resource_class_kwargs={})
