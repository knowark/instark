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


def test_notification_coordinator_instantiation(
        notification_coordinator: NotificationCoordinator):
    assert notification_coordinator is not None


async def test_notification_coordinator_send_direct_message(
        notification_coordinator: NotificationCoordinator) -> None:
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


async def test_notification_coordinator_send_direct_message_failed(
        notification_coordinator: NotificationCoordinator):
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
        notification_coordinator: NotificationCoordinator):
    notification_coordinator.delivery_service.response = 'BROADCAST'
    notification_coordinator.channel_repository.load({
        'default': {
            '1': Channel(**{'id': '1', 'name': 'Channel XYZ', 'code': 'news'})
        }
    })
    message_records: RecordList = [{
        'recipient_id': '1',
        'kind': 'Channel',
        'content': 'Hello'
    }]

    await notification_coordinator.send_message(message_records)

    assert len(
        await notification_coordinator.message_repository.search([])) == 1

    for message in await notification_coordinator.message_repository.search([]):
        assert message.recipient_id == '1'
        assert message.kind == 'Channel'


async def test_notification_coordinator_delete_message(
        notification_coordinator: NotificationCoordinator) -> None:
    notification_coordinator.delivery_service.response = 'BROADCAST'
    notification_coordinator.channel_repository.load({
        'default': {
            '1': Channel(**{'id': '1', 'name': 'Channel XYZ', 'code': 'news'})
        }
    })
    message_id = '07506ce5-edd7-4eab-af9c-4e555bc8e098'
    message_records: RecordList = [{
        'id': message_id,
        'recipient_id': '1',
        'kind': 'Channel',
        'content': 'Hello'
    }]
    await notification_coordinator.send_message(message_records)
    messages_data = getattr(
        notification_coordinator.message_repository, 'data')
    assert len(messages_data['default']) == 1
    await notification_coordinator.delete_message([message_id])
    assert len(messages_data['default']) == 0
