from typing import Any
from aiohttp import web
from injectark import Injectark
from .resources import(
    RootResource, MessageResource, ChannelResource,
    DeviceResource, SubscriptionResource)
from .spec import create_spec


def create_api(app: web.Application, injector: Injectark) -> None:
    # Restful API
    spec = create_spec()

    # Root Resource
    bind_routes(app, '/', RootResource(spec))

    # Channel Resource
    bind_routes(app, '/channels', ChannelResource(injector))
    spec.path(path="/channels", operations={
    'head': {}, 'get': {}, 'post': {}},resource=ChannelResource)

    # Device Resource
    bind_routes(app, '/devices', DeviceResource(injector))
    spec.path(path="/devices", operations={
    'head': {}, 'get': {}, 'put': {}},resource=DeviceResource)

    # Message Resource
    bind_routes(app, '/messages', MessageResource(injector))
    spec.path(path="/messages", operations={
    'head': {}, 'get': {}, 'put': {}}, resource=MessageResource)

    # Subscription Resource
    bind_routes(app, '/subscriptions', SubscriptionResource(injector))
    spec.path(path="/subscriptions", operations={
    'head': {}, 'get': {}, 'post': {}},resource=SubscriptionResource)



def bind_routes(app: web.Application, path: str, resource: Any):
    general_methods = ['head', 'get', 'put', 'delete', 'post', 'patch']
    identified_methods = ['get', 'delete']
    for method in general_methods + identified_methods:
        handler = getattr(resource, method, None)
        if not handler:
            continue
        if method in identified_methods:
            app.router.add_route(method, path + "/{id}", handler)
        if method in general_methods:
            app.router.add_route(method, path, handler)

    """# Message Resource
    spec.path(path="/messages", resource=MessageResource)
    message_view = authenticate(MessageResource.as_view(
        'messages', injector=injector))
    app.add_url_rule("/messages", view_func=message_view)

    # Channel Resource
    spec.path(path="/channels", resource=ChannelResource)
    channel_view = authenticate(ChannelResource.as_view(
        'channels', injector=injector))
    app.add_url_rule("/channels", view_func=channel_view)

    # Device Resource
    spec.path(path="/devices", resource=DeviceResource)
    device_view = authenticate(DeviceResource.as_view(
        'devices', injector=injector))
    app.add_url_rule("/devices", view_func=device_view)

    # Subscription Resource
    spec.path(path="/subscriptions", resource=SubscriptionResource)
    subscription_view = authenticate(SubscriptionResource.as_view(
        'subscriptions', injector=injector))
    app.add_url_rule("/subscriptions", view_func=subscription_view)"""
