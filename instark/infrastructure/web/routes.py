from flask import Flask
from flask_restful import Api
from flask_restful_swagger import swagger
from ..config import Registry
from .resources import DeviceResource, ChannelResource, SubscriptionResource


def set_routes(app: Flask, registry: Registry) -> None:

    @app.route('/')
    def index() -> str:
        return ('Welcome to Instark!<br/>'
                '<a href="/spec.html">spec</a>')

    # Restful API
    api = swagger.docs(Api(app), apiVersion='1.0',
                       api_spec_url='/spec', swaggerVersion='3.0.2')

    # Devices Resource
    api.add_resource(DeviceResource, '/devices',
                     resource_class_kwargs=registry)

    # Channels Resource
    api.add_resource(ChannelResource, '/channels',
                     resource_class_kwargs=registry)

    # Subscriptions Resource
    api.add_resource(SubscriptionResource, '/subscriptions',
                     resource_class_kwargs=registry)
