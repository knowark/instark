from pytest import fixture, raises
from instark.application.domain.models import Device, Channel
from instark.application.managers import NotificationManager
from instark.application.domain.common import RecordList
from instark.application.domain.repositories import (
    MemoryChannelRepository, MemoryDeviceRepository,
    MemorySubscriptionRepository, MemoryMessageRepository)
from instark.application.domain.common import (
    QueryParser, StandardTenantProvider, Tenant)


@fixture
def notification_manager(channel_repository, device_repository,
                         message_repository, delivery_service):
    return NotificationManager(channel_repository,
                               device_repository, message_repository,
                               delivery_service)


def test_notification_manager_instantiation(
        notification_manager: NotificationManager):
    assert notification_manager is not None


async def test_notification_manager_send_direct_message(
        notification_manager: NotificationManager) -> None:
    notification_manager.delivery_service.response = 'a1b2c3'
    notification_manager.device_repository.load({
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

    await notification_manager.send_message(message_dicts)
    items = getattr(
        notification_manager.message_repository, 'data')['default']
    assert len(items) == 1


async def test_notification_manager_send_direct_message_failed(
        notification_manager: NotificationManager):
    notification_manager.device_repository.load({
        'default': {
            '1': Device(**{'id': '1', 'name': 'Device 1', 'locator': 'ABC123'})
        }
    })
    message_dicts: RecordList = [{
        'recipient_id': '1',
        'kind': 'Direct',
        'content': 'Hello'
    }]
    notification_manager.delivery_service.response = ''

    with raises(ValueError):
        await notification_manager.send_message(message_dicts)


async def test_notification_manager_send_channel_message(
        notification_manager: NotificationManager):
    notification_manager.delivery_service.response = 'BROADCAST'
    notification_manager.channel_repository.load({
        'default': {
            '1': Channel(**{'id': '1', 'name': 'Channel XYZ', 'code': 'news'})
        }
    })
    message_records: RecordList = [{
        'recipient_id': '1',
        'kind': 'Channel',
        'content': 'Hello'
    }]

    await notification_manager.send_message(message_records)

    assert len(
        await notification_manager.message_repository.search([])) == 1

    for message in await notification_manager.message_repository.search([]):
        assert message.recipient_id == '1'
        assert message.kind == 'Channel'


async def test_notification_manager_delete_message(
        notification_manager: NotificationManager) -> None:
    notification_manager.delivery_service.response = 'BROADCAST'
    notification_manager.channel_repository.load({
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
    await notification_manager.send_message(message_records)
    messages_data = getattr(
        notification_manager.message_repository, 'data')
    assert len(messages_data['default']) == 1
    await notification_manager.delete_message([message_id])
    assert len(messages_data['default']) == 0
