from flask import Flask, jsonify
from injectark import Injectark
from .middleware import Authenticate
from .resources import(
    RootResource, MessageResource, ChannelResource,
    DeviceResource, SubscriptionResource)
from .spec import create_spec


def create_api(app: Flask, resolver: Injectark) -> None:

    # Restful API
    spec = create_spec()

    # Root Resource (Api Specification)
    root_view = RootResource.as_view('root', spec=spec)
    app.add_url_rule("/", view_func=root_view)

    # Middleware
    authenticate = resolver.resolve('Authenticate')

    # Message Resource
    spec.path(path="/messages/", resource=MessageResource)
    message_view = authenticate(MessageResource.as_view(
        'messages', resolver=resolver))
    app.add_url_rule("/messages/", view_func=message_view)

    # Channel Resource
    spec.path(path="/channels/", resource=ChannelResource)
    channel_view = authenticate(ChannelResource.as_view(
        'channels', resolver=resolver))
    app.add_url_rule("/channels/", view_func=channel_view)

    # Device Resource
    spec.path(path="/devices/", resource=DeviceResource)
    device_view = authenticate(DeviceResource.as_view(
        'devices', resolver=resolver))
    app.add_url_rule("/devices/", view_func=device_view)

    # Subscription Resource
    spec.path(path="/subscriptions/", resource=SubscriptionResource)
    subscription_view = authenticate(SubscriptionResource.as_view(
        'subscriptions', resolver=resolver))
    app.add_url_rule("/subscriptions/", view_func=subscription_view)
