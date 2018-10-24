from flask import Flask
from ..config import Registry
# from .resources import DeviceResource, ChannelResource, SubscriptionResource
from flask_restplus import Api, Namespace, Resource
from .resources import channel_namespace, ChannelResource


def create_api(app: Flask, registry: Registry) -> Api:

    # @app.route('/')
    # def index() -> str:
    #     return ('Welcome to Instark!<br/>'
    #             '<a href="/spec.html">spec</a>')

    # REST API
    api = Api(title='Instark', version='1.0')

    # # Devices Resource
    # api.add_resource(DeviceResource, '/devices',
    #                  resource_class_kwargs=registry)

    # Channels Resource
    # api.add_resource(ChannelResource, '/channels',
    #                  resource_class_kwargs=registry)

    register_resource(channel_namespace, ChannelResource,
                      '/channels', registry)

    # # Subscriptions Resource
    # api.add_resource(SubscriptionResource, '/subscriptions',
    #                  resource_class_kwargs=registry)

    # Add namespaces
    api.add_namespace(channel_namespace)

    return api


def register_resource(namespace: Namespace, resource: Resource,
                      path: str, arguments: dict):
    namespace.add_resource(ChannelResource, endpoint=path,
                           resource_class_kwargs=arguments)
