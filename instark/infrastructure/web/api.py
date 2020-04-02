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
        'head': {}, 'get': {}, 'put': {}, 'delete': {}},
        resource=ChannelResource)

    # Device Resource
    bind_routes(app, '/devices', DeviceResource(injector))
    spec.path(path="/devices", operations={
        'head': {}, 'get': {}, 'put': {}, 'delete': {}},
        resource=DeviceResource)

    # Message Resource
    bind_routes(app, '/messages', MessageResource(injector))
    spec.path(path="/messages", operations={
        'head': {}, 'get': {}, 'put': {}, 'delete': {}},
        resource=MessageResource)

    # Subscription Resource
    bind_routes(app, '/subscriptions', SubscriptionResource(injector))
    spec.path(path="/subscriptions", operations={
        'head': {}, 'get': {}, 'put': {}, 'delete': {}},
        resource=SubscriptionResource)


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
