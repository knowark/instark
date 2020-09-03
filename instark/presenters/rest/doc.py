from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from .helpers.schemas import (
    ChannelSchema, DeviceSchema, MessageSchema, SubscriptionSchema,
    UserSchema)


def create_spec() -> APISpec:
    spec = APISpec(
        title="Instark",
        version="1.0.0",
        openapi_version="3.0.2",
        plugins=[MarshmallowPlugin()],
        info=dict(
            description="Proser Server",
            contact=dict(
                name="Knowark",
                url="https://www.knowark.com"
            )))

    _register_schemas(spec)
    _register_paths(spec)

    return spec


def _register_schemas(spec):
    spec.components.schema("Channel", schema=ChannelSchema)
    spec.components.schema("Device", schema=DeviceSchema)
    spec.components.schema("Message", schema=MessageSchema)
    spec.components.schema("Subscription", schema=SubscriptionSchema)
    spec.components.schema("User", schema=UserSchema)


def _register_paths(spec):
    resources = [
        ('activities', 'Channel'),
        ('Devices', 'Device'),
        ('Messages', 'Message'),
        ('Subscription', 'Subscription'),
        ('occurrences', 'Occurrence'),
        ('reviews', 'Review'),
        ('sites', 'Site'),
        ('traces', 'Trace'),
        ('users', 'User'),
    ]
    for resource in resources:
        _append_path(spec, *resource)


def _append_path(spec, endpoint, schema):
    spec.path(
        path=f'/{endpoint}',
        operations={
            'get': {
                'tags': [schema],
                'responses': _respond(f"Get all {endpoint}", schema)
            },
            'put': {
                'tags': [schema],
                'responses': _respond(f"Modify {endpoint}", schema)
            },
            'delete': {
                'tags': [schema],
                'responses': _respond(f"Delete {endpoint}", schema)
            }
        }
    )


def _respond(description, schema, status='200'):
    return {
        status: {
            "description": description,
            "content": {
                "application/json": {
                    "schema": {
                        "type": "array",
                        "items": {
                            "$ref": f"#/components/schemas/{schema}"
                        }
                    }
                }
            }
        }
    }
