from pytest import fixture
from instark.application.domain.models import Device, Channel, Message
from instark.application.managers import SubscriptionManager
from instark.application.domain.common import RecordList
from instark.application.domain.repositories import (
    MemoryChannelRepository, MemoryDeviceRepository,
    MemoryMessageRepository, MemorySubscriptionRepository)
from instark.application.domain.common import (
    QueryParser, StandardTenantProvider, Tenant)


@fixture
def subscription_manager(channel_repository, device_repository,
                         message_repository, subscription_repository,
                         delivery_service):
    subscription_manager = SubscriptionManager(
        channel_repository, device_repository, message_repository,
        subscription_repository, delivery_service)
    subscription_manager.channel_repository.load({
        'default': {
            '001': Channel(id='001', name='Surveillance', code='surveillance')
        }
    })
    subscription_manager.device_repository.load({
        'default': {
            '001': Device(id='001', name='Android SSX10', locator='ABC123')
        }
    })
    return subscription_manager


def test_subscription_manager_instantiation(
        subscription_manager: SubscriptionManager) -> None:
    assert subscription_manager is not None


async def test_channel_manager_create_channel(
        subscription_manager: SubscriptionManager) -> None:
    channel_dicts: RecordList = [{
        'name': 'Channel 2',
        'code': 'CH002'
    }]
    await subscription_manager.create_channel(channel_dicts)


async def test_subscription_manager_delete_channel_with_message(
        subscription_manager: SubscriptionManager) -> None:
    channel_id = '07506ce5-edd7-4eab-af9c-4e555bc8e098'
    channel_records: RecordList = [{
        'id': channel_id,
        'name': 'Channel 3',
        'code': 'CH003'
    }]

    await subscription_manager.create_channel(channel_records)

    subscription_manager.message_repository.load({
        'default': {
            '001': Message(id='001',
                           recipient_id=channel_id,
                           content='Hello world',
                           kind='channel')
        }
    })

    channels_data = getattr(
        subscription_manager.channel_repository, 'data')

    assert len(channels_data['default']) == 2
    result = await subscription_manager.delete_channel([channel_id])


async def test_subscription_manager_delete_channel_without_message(
        subscription_manager: SubscriptionManager) -> None:
    channel_id = '07506ce5-edd7-4eab-af9c-4e555bc8e098'
    channel_records: RecordList = [{
        'id': channel_id,
        'name': 'Channel 3',
        'code': 'CH003'
    }]
    await subscription_manager.create_channel(channel_records)
    channels_data = getattr(
        subscription_manager.channel_repository, 'data')
    assert len(channels_data['default']) == 2
    await subscription_manager.delete_channel([channel_id])
    assert len(channels_data['default']) == 1  # line 19


async def test_subscription_manager_delete_channel_without_ids(
        subscription_manager: SubscriptionManager) -> None:
    channel_id = ''
    await subscription_manager.delete_channel([channel_id])


async def test_subscription_manager_subscribe(
        subscription_manager: SubscriptionManager) -> None:
    subscription_dicts: RecordList = [{
        'device_id': '001',
        'channel_id': '001'
    }]
    await subscription_manager.subscribe(subscription_dicts)
    assert len(subscription_manager.subscription_repository.data) == 1


async def test_subscription_manager_delete_subscription(
        subscription_manager: SubscriptionManager) -> None:
    subscription_id = '07506ce5-edd7-4eab-af9c-4e555bc8e098'
    subscription_records: RecordList = [{
        'id': subscription_id,
        'device_id': '001',
        'channel_id': '001'
    }]
    await subscription_manager.subscribe(subscription_records)
    subscriptions_data = getattr(
        subscription_manager.subscription_repository, 'data')
    assert len(subscriptions_data['default']) == 1
    await subscription_manager.delete_subscribe([subscription_id])
    assert len(subscriptions_data['default']) == 0
