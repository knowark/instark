from pytest import raises
from rapidjson import loads, dumps
from aiohttp import web

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


async def test_channels_post(app, headers) -> None:
    channel_data = dumps([{
        "id": "1", 
        "channel_name": "General Notifications", 
        "channel_code": "CH001"
    }])
    response = await app.post('/channels',
                             data=channel_data, headers=headers)
    content = await response.text()
    assert response.status == 200


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
        'device_name': 'DEV1', 
        'device_locator': 'a1b2c3d4'
    }])
    response = await app.put('/devices',
                             data=device_data, headers=headers)
    content = await response.text()
    assert response.status == 201


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

    device_data = dumps([ {
        'id': '1', 
        'device_name': 'DEV1', 
        'device_locator': 'a1b2c3d4'
    } ])
    response = await app.put('/devices',
                             data=device_data, headers=headers)

    message_data = dumps([ {
        'id': '1', 
        'recipientId': '1', 
        'kind': 'Direct',
        'content': 'Hello World', 
        'title': 'Message Direct of admin'
    } ])
    response = await app.put('/messages',
                             data=message_data, headers=headers)

    content = await response.text()
    assert response.status == 201

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


async def test_subscriptions_post(app, headers) -> None:
    channel_data = dumps([ {
        "id": "1", 
        "channel_name": "Channel 1", 
        "channel_code": "CH1"
    }])
    response = await app.post('/channels',
                             data=channel_data, headers=headers)

    device_data = dumps([ {
        'id': '1', 
        'device_name': 'DEV1', 
        'device_locator': 'a1b2c3d4'} 
    ])
    response = await app.put('/devices',
                             data=device_data, headers=headers)
                                                      
    subscription_data = dumps([ {
        'id': '1', 
        'channelId': '1', 
        'deviceId': '1'
    } ])
    response = await app.post('/subscriptions',
                             data=subscription_data, headers=headers)
    content = await response.text()
    assert response.status == 200

"""
# Channels


# Devices


def test_device_post_action(app: Flask, headers: dict) -> None:
    device = {'id': '1', 'name': 'DEV1', 'locator': 'a1b2c3d4'}
    response = app.put('/devices', headers=headers, data=dumps(device),
                       content_type='application/json')
    assert response
    assert response.status == '201 CREATED'

# Messages


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
    assert response.status == '201 CREATED' """
