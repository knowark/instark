from pytest import fixture, raises
from instark.application.models import Device, Channel
from instark.application.coordinators import NotificationCoordinator
from instark.application.repositories import (
    MemoryChannelRepository, MemoryDeviceRepository,
    MemorySubscriptionRepository, MemoryMessageRepository)
from instark.application.utilities import (
    QueryParser, StandardTenantProvider, Tenant)


@fixture
def notification_coordinator(channel_repository, device_repository,
                             message_repository, delivery_service):
    return NotificationCoordinator(channel_repository,
                                   device_repository, message_repository,
                                   delivery_service)


def test_notification_coordinator_instantiation(notification_coordinator):
    assert notification_coordinator is not None


async def test_notification_coordinator_send_direct_message(
        notification_coordinator) -> None:
    notification_coordinator.delivery_service.response = 'a1b2c3'
    notification_coordinator.device_repository.load({
        "default": {
            "1": Device(id='1', name='Device 1', locator='ABC123')
        }
    })
    message_dicts: RecordList = [{
        'recipient_id': '1',
        'kind': 'direct',
        'content': 'Hello',
        'title': 'Tittle notification'
    }]

    await notification_coordinator.send_message(message_dicts)
    items = getattr(
        notification_coordinator.message_repository, 'data')['default']
    assert len(items) == 1

    #assert len(await notification_coordinator.message_repository.search([])) == 1


async def test_notification_coordinator_send_direct_message_failed(
        notification_coordinator):
    notification_coordinator.device_repository.load({
        'default': {
            '1': Device(**{'id': '1', 'name': 'Device 1', 'locator': 'ABC123'})
        }
    })
    message_dicts: RecordList = [{
        'recipient_id': '1', 
        'kind': 'Direct', 
        'content': 'Hello'
    }]
    notification_coordinator.delivery_service.response = ''

    with raises(ValueError):
        await notification_coordinator.send_message(message_dicts)


async def test_notification_coordinator_send_channel_message(
        notification_coordinator):
    notification_coordinator.delivery_service.response = 'BROADCAST'
    notification_coordinator.channel_repository.load({
        'default': {
            '1': Channel(**{'id': '1', 'name': 'Channel XYZ', 'code': 'news'})
        }
    })
    message_dicts: RecordList= [{
        'recipient_id': '1', 
        'kind': 'Channel', 
        'content': 'Hello'
    }]

    await notification_coordinator.send_message(message_dicts)

    assert len(await notification_coordinator.message_repository.search([])) == 1

    for message in await notification_coordinator.message_repository.search([]):
        assert message.recipient_id == '1'
        assert message.kind == 'Channel'
