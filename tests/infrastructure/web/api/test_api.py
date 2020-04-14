from pytest import raises
from rapidjson import loads, dumps
from aiohttp import web
from instark.infrastructure.web.middleware import (
    authenticate_middleware_factory)


async def test_root(app) -> None:
    response = await app.get('/')

    content = await response.text()

    assert response.status == 200
    assert 'Instark' in content


async def test_root_api(app) -> None:
    response = await app.get('/?api')
    data = await response.text()
    api = loads(data)

    assert 'openapi' in api
    assert api['info']['title'] == 'Instark'

# Channels


async def test_channels_head(app, headers) -> None:
    response = await app.head('/channels', headers=headers)
    count = response.headers.get('Total-Count')

    assert int(count) == 3


async def test_channels_get(app, headers) -> None:
    response = await app.get('/channels', headers=headers)
    content = await response.text()

    assert response.status == 200

    data_dict = loads(content)

    assert len(data_dict) == 3
    assert data_dict[0]['id'] == '001'


async def test_channels_put(app, headers) -> None:
    channel_data = dumps([{
        "id": "1",
        "name": "General Notifications",
        "code": "CH001"
    }])
    response = await app.put('/channels',
                             data=channel_data, headers=headers)
    content = await response.text()
    assert response.status == 201


async def test_channels_delete(app, headers) -> None:
    response = await app.delete('/channels/001', headers=headers)
    content = await response.text()
    assert response.status == 204

    response = await app.get('/channels', headers=headers)
    data_dict = loads(await response.text())

    assert len(data_dict) == 2


async def test_channels_delete_body(app, headers) -> None:
    ids = dumps(["001"])
    response = await app.delete(
        '/channels', data=ids, headers=headers)
    content = await response.text()
    assert response.status == 204

    response = await app.get('/channels', headers=headers)
    data_dict = loads(await response.text())

    assert len(data_dict) == 2

# Devices


async def test_devices_head(app, headers) -> None:
    response = await app.head('/devices', headers=headers)
    count = response.headers.get('Total-Count')

    assert int(count) == 2


async def test_devices_get(app, headers) -> None:
    response = await app.get('/devices', headers=headers)
    content = await response.text()

    assert response.status == 200

    data_dict = loads(content)

    assert len(data_dict) == 2
    assert data_dict[0]['id'] == '001'


async def test_devices_put(app, headers) -> None:
    device_data = dumps([{
        'id': '1',
        'name': 'DEV1',
        'locator': 'a1b2c3d4'
    }])
    response = await app.put('/devices',
                             data=device_data, headers=headers)
    content = await response.text()
    assert response.status == 201


async def test_devices_delete(app, headers) -> None:
    response = await app.delete('/devices/001', headers=headers)
    content = await response.text()
    assert response.status == 204

    response = await app.get('/devices', headers=headers)
    data_dict = loads(await response.text())

    assert len(data_dict) == 2


async def test_devices_delete_body(app, headers) -> None:
    ids = dumps(["001"])
    response = await app.delete(
        '/devices', data=ids, headers=headers)
    content = await response.text()
    assert response.status == 204

    response = await app.get('/devices', headers=headers)
    data_dict = loads(await response.text())

    assert len(data_dict) == 2

# Messages


async def test_messages_head(app, headers) -> None:
    response = await app.head('/messages', headers=headers)
    count = response.headers.get('Total-Count')

    assert int(count) == 1


async def test_messages_get(app, headers) -> None:
    response = await app.get('/messages', headers=headers)
    content = await response.text()

    assert response.status == 200

    data_dict = loads(content)

    assert len(data_dict) == 1
    assert data_dict[0]['id'] == '001'


async def test_messages_put(app, headers) -> None:

    device_data = dumps([{
        'id': '1',
        'name': 'DEV1',
        'locator': 'a1b2c3d4'
    }])
    response = await app.put('/devices',
                             data=device_data, headers=headers)

    message_data = dumps([{
        'id': '1',
        'recipientId': '1',
        'kind': 'direct',
        'content': 'Hello World',
        'title': 'Message Direct of admin'
    }])
    response = await app.put('/messages',
                             data=message_data, headers=headers)

    content = await response.text()
    assert response.status == 201


async def test_messages_delete(app, headers) -> None:
    response = await app.delete('/messages/001', headers=headers)
    content = await response.text()
    assert response.status == 204

    response = await app.get('/messages', headers=headers)
    data_dict = loads(await response.text())

    assert len(data_dict) == 0


async def test_messages_delete_body(app, headers) -> None:
    ids = dumps(["001"])
    response = await app.delete(
        '/messages', data=ids, headers=headers)
    content = await response.text()
    assert response.status == 204

    response = await app.get('/messages', headers=headers)
    data_dict = loads(await response.text())

    assert len(data_dict) == 0

# Subscriptions


async def test_subscriptions_head(app, headers) -> None:
    response = await app.head('/subscriptions', headers=headers)
    count = response.headers.get('Total-Count')

    assert int(count) == 2


async def test_subscriptions_get(app, headers) -> None:
    response = await app.get('/subscriptions', headers=headers)
    content = await response.text()

    assert response.status == 200

    data_dict = loads(content)

    assert len(data_dict) == 2
    assert data_dict[0]['id'] == '001'


async def test_subscriptions_put(app, headers) -> None:
    channel_data = dumps([{
        "id": "1",
        "name": "Channel 1",
        "code": "CH1"
    }])
    response = await app.put('/channels',
                             data=channel_data, headers=headers)

    device_data = dumps([{
        'id': '1',
        'name': 'DEV1',
        'locator': 'a1b2c3d4'}
    ])
    response = await app.put('/devices',
                             data=device_data, headers=headers)

    subscription_data = dumps([{
        'id': '1',
        'channelId': '1',
        'deviceId': '1'
    }])
    response = await app.put('/subscriptions',
                             data=subscription_data, headers=headers)
    content = await response.text()
    assert response.status == 201


async def test_subscriptions_delete(app, headers) -> None:
    response = await app.delete('/subscriptions/001', headers=headers)
    content = await response.text()
    assert response.status == 204

    response = await app.get('/subscriptions', headers=headers)
    data_dict = loads(await response.text())

    assert len(data_dict) == 1


async def test_subscriptions_delete_body(app, headers) -> None:
    ids = dumps(["001"])
    response = await app.delete(
        '/subscriptions', data=ids, headers=headers)
    content = await response.text()
    assert response.status == 204

    response = await app.get('/subscriptions', headers=headers)
    data_dict = loads(await response.text())

    assert len(data_dict) == 1

# filter


async def test_get_request_filter(app, headers) -> None:
    response = await app.get(
        '/channels?filter=[["name", "=", "Channel 3"]]',
        headers=headers)
    content = await response.text()
    data_dict = loads(content)
    assert len(data_dict) == 1

# middleware


async def test_channels_get_unauthorized(app) -> None:
    response = await app.get('/channels')
    content = await response.text()

    assert response.status == 401
    data_dict = loads(content)
    assert 'error' in data_dict
