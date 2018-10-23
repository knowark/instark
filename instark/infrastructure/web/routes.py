from flask import Flask
from flask_restful import Api
from ..config import Registry
from .resources import DeviceResource, ChannelResource, SubscriptionResource


def set_routes(app: Flask, registry: Registry) -> None:

    @app.route('/')
    def index() -> str:
        return "Welcome to Instark!"

    # Restful API
    api = Api(app)

    # Devices Resource
    api.add_resource(DeviceResource, '/devices',
                     resource_class_kwargs=registry)

    # Channels Resource
    api.add_resource(ChannelResource, '/channels',
                     resource_class_kwargs=registry)

    # Subscriptions Resource
    api.add_resource(SubscriptionResource, '/subscriptions',
                     resource_class_kwargs=registry)
