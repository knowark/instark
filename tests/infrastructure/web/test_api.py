from pytest import raises
from flask import Flask, request
from json import loads, dumps
from instark.infrastructure.core.common.exceptions import AuthenticationError
from instark.infrastructure.core.configuration import ProductionConfig


def test_production_config_retrieve() -> None:
    assert ProductionConfig()["mode"] == "PROD"


def test_root_resource(app: Flask, headers: dict) -> None:
    response = app.get('/', headers=headers)
    data = str(response.data, 'utf-8')
    assert data is not None


def test_root_resource_request_none(app: Flask, headers: dict) -> None:
    response = app.get('/?api', headers=headers)
    data = str(response.data, 'utf-8')
    assert data is not None


def test_invalid_headers(app: Flask) -> None:
    with raises(AuthenticationError):
        response = app.get('/messages')
        data = loads(str(response.data, 'utf-8'))
        assert data["error"] is not None


# Channels

def test_all_channels_get_action(app: Flask, headers: dict) -> None:
    response = app.get('/channels', headers=headers)
    data = str(response.data, 'utf-8')
    data = loads(data)

    assert len(data) == 0


def test_channel_post_action(app: Flask, headers: dict) -> None:
    channel = {"id": "1", "name": "Channel 1", "code": "CH1"}
    response = app.post('/channels', headers=headers, data=dumps(channel),
                        content_type='application/json')
    assert response
    assert response.status == '201 CREATED'

# Devices


def test_all_devices_get_action(app: Flask, headers: dict) -> None:
    response = app.get('/devices', headers=headers)
    data = str(response.data, 'utf-8')
    data = loads(data)

    assert len(data) == 0


def test_device_post_action(app: Flask, headers: dict) -> None:
    device = {'id': '1', 'name': 'DEV1', 'locator': 'a1b2c3d4'}
    response = app.put('/devices', headers=headers, data=dumps(device),
                       content_type='application/json')
    assert response
    assert response.status == '201 CREATED'

# Messages


def test_all_messages_get_action(app: Flask, headers: dict) -> None:
    response = app.get('/messages', headers=headers)
    data = str(response.data, 'utf-8')
    data = loads(data)

    assert len(data) == 0


def test_message_post_action(app: Flask, headers: dict) -> None:
    device = {'id': '1', 'name': 'DEV1', 'locator': 'a1b2c3d4'}
    app.put('/devices', headers=headers, data=dumps(device),
            content_type='application/json')
    message = {'id': '1', 'recipientId': '1', 'kind': 'Direct',
               'content': 'Hello World', 'title': 'Message Direct of admin'}
    response = app.post('/messages', headers=headers, data=dumps(message),
                        content_type='application/json')
    assert response
    assert response.status == '201 CREATED'

# Subscriptions


def test_all_subscriptions_get_action(app: Flask, headers: dict) -> None:
    response = app.get('/subscriptions', headers=headers)
    data = str(response.data, 'utf-8')
    data = loads(data)

    assert len(data) == 0


def test_subscription_post_action(app: Flask, headers: dict) -> None:
    channel = {"id": "1", "name": "Channel 1", "code": "CH1"}
    response = app.post('/channels', headers=headers, data=dumps(channel),
                        content_type='application/json')
    device = {'id': '1', 'name': 'DEV1', 'locator': 'a1b2c3d4'}
    app.put('/devices', headers=headers, data=dumps(device),
            content_type='application/json')
    subscription = {'id': '1', 'channelId': '1', 'deviceId': '1'}
    response = app.post(
        '/subscriptions', headers=headers, data=dumps(subscription),
        content_type='application/json')
    assert response
    assert response.status == '201 CREATED'
