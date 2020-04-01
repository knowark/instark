from pytest import fixture
from instark.application.models import Device, Channel
from instark.application.coordinators import SubscriptionCoordinator
from instark.application.repositories import (
    MemoryChannelRepository, MemoryDeviceRepository,
    MemorySubscriptionRepository)
from instark.application.utilities import (
    QueryParser, StandardTenantProvider, Tenant)


@fixture
def subscription_coordinator(channel_repository,
                             device_repository, subscription_repository,
                             delivery_service):
    subscription_coordinator = SubscriptionCoordinator(
        channel_repository, device_repository,
        subscription_repository, delivery_service)
    subscription_coordinator.channel_repository.load({
        'default': {
            '001': Channel(id='001', name='Surveillance', code='surveillance')
        }
    })
    subscription_coordinator.device_repository.load({
        'default': {
            '001': Device(id='001', name='Android SSX10', locator='ABC123')
        }
    })
    return subscription_coordinator


def test_subscription_coordinator_instantiation(
        subscription_coordinator: SubscriptionCoordinator) -> None:
    assert subscription_coordinator is not None


async def test_channel_coordinator_create_channel(
        subscription_coordinator: SubscriptionCoordinator) -> None:
    channel_dicts: RecordList = [{
        'name': 'Channel 2',
        'code': 'CH002'
    }]
    await subscription_coordinator.create_channel(channel_dicts)


async def test_subscription_coordinator_delete_channel(
        subscription_coordinator: SubscriptionCoordinator) -> None:
    channel_id = '07506ce5-edd7-4eab-af9c-4e555bc8e098'
    channel_records: RecordList = [{
        'id': channel_id,
        'name': 'Channel 3',
        'code': 'CH003'
    }]
    await subscription_coordinator.create_channel(channel_records)
    channels_data = getattr(
        subscription_coordinator.channel_repository, 'data')
    assert len(channels_data['default']) == 2
    await subscription_coordinator.delete_channel([channel_id])
    assert len(channels_data['default']) == 1  # line 19


async def test_subscription_coordinator_subscribe(
        subscription_coordinator: SubscriptionCoordinator) -> None:
    subscription_dicts: RecordList = [{
        'device_id': '001',
        'channel_id': '001'
    }]
    await subscription_coordinator.subscribe(subscription_dicts)
    assert len(subscription_coordinator.subscription_repository.data) == 1


async def test_subscription_coordinator_delete_subscription(
        subscription_coordinator: SubscriptionCoordinator) -> None:
    subscription_id = '07506ce5-edd7-4eab-af9c-4e555bc8e098'
    subscription_records: RecordList = [{
        'id': subscription_id,
        'device_id': '001',
        'channel_id': '001'
    }]
    await subscription_coordinator.subscribe(subscription_records)
    subscriptions_data = getattr(
        subscription_coordinator.subscription_repository, 'data')
    assert len(subscriptions_data['default']) == 1
    print("subscription data:   ", subscriptions_data)
    await subscription_coordinator.delete_subscribe([subscription_id])
    assert len(subscriptions_data['default']) == 0
