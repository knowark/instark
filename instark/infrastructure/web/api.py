from flask import Flask
from ..config import Registry
from flask_restful import Api, Resource
from flasgger import Swagger, swag_from
from .resources import (
    DeviceResource, ChannelResource, SubscriptionResource, MessageResource)


def create_api(app: Flask, registry: Registry) -> Api:

    # REST API
    api = Api(app)

    # Swagger
    Swagger(app, template_file="api.yml", config={
        "specs_route": "/",
        "headers": [],
        "specs": [{
            "endpoint": 'apispec_1',
            "route": '/apispec_1.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True
    })

    # Devices Resource
    api.add_resource(DeviceResource, '/devices',
                     resource_class_kwargs=registry)

    # Channels Resource
    api.add_resource(ChannelResource, '/channels',
                     resource_class_kwargs=registry)

    # Subscriptions Resource
    api.add_resource(SubscriptionResource, '/subscriptions',
                     resource_class_kwargs=registry)

    # Messages Resource
    api.add_resource(MessageResource, '/messages',
                     resource_class_kwargs=registry)

    return api
