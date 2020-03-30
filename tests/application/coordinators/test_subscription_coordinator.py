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


def test_subscription_coordinator_instantiation(subscription_coordinator):
    assert subscription_coordinator is not None


async def test_channel_coordinator_create_channel(subscription_coordinator):
    channel_dicts: RecordList = [{
        'name': 'Channel 2', 
        'code': 'CH002'
    }]
    await subscription_coordinator.create_channel(channel_dicts)

# def test_get_channels(subscription_coordinator):
#     channel_dict = {'id': '001', 'name': 'Channel 1', 'code': 'CH001'}
#     subscription_coordinator.get_channels(channel_dict['id'])
#     assert len(subscription_coordinator.channel_repository.items) > 0


async def test_subscription_coordinator_subscribe(subscription_coordinator):
    subscription_dicts: RecordList = [{
        'device_id': '001', 
        'channel_id': '001'
    }]
    await subscription_coordinator.subscribe(subscription_dicts)
    assert len(subscription_coordinator.subscription_repository.data) == 1


# def test_subscription_coordinator_subscribe_delivery_service(
#         subscription_coordinator):
#     code = 'surveillance'
#     locator = 'ABC123'
#     subscription_dict = {'device_id': '001', 'channel_id': '001'}
#     subscription_coordinator.subscribe(subscription_dict)

#     assert subscription_coordinator.delivery_service.code == code
#     assert subscription_coordinator.delivery_service.locator == locator
