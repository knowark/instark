from pytest import fixture
from instark.application.models import Device, Channel
from instark.application.coordinators import SubscriptionCoordinator
from instark.application.repositories import (
    MemoryChannelRepository, MemoryDeviceRepository, MemorySubscriptionRepository)
from instark.application.utilities import (
    QueryParser, StandardTenantProvider, Tenant)


@fixture
def channel_repository() -> MemoryChannelRepository:
    tenant_provider = StandardTenantProvider(Tenant(name="Default"))
    parser = QueryParser()
    channel_repository = MemoryChannelRepository(parser, tenant_provider)
    return channel_repository

@fixture
def device_repository() -> MemoryDeviceRepository:
    tenant_provider = StandardTenantProvider(Tenant(name="Default"))
    parser = QueryParser()
    device_repository = MemoryDeviceRepository(parser, tenant_provider)
    return device_repository

@fixture
def device_channel_repository() -> MemorySubscriptionRepository:
    tenant_provider = StandardTenantProvider(Tenant(name="Default"))
    parser = QueryParser()
    device_channel_repository = MemorySubscriptionRepository(parser, tenant_provider)
    return device_channel_repository

@fixture
def subscription_coordinator(id_service, channel_repository,
                             device_repository, device_channel_repository,
                             delivery_service):
    subscription_coordinator = SubscriptionCoordinator(
        id_service, channel_repository, device_repository,
        device_channel_repository, delivery_service)
    subscription_coordinator.channel_repository.load({
        'default' : {
            '001': Channel(**{'id':'001', 'name':'Surveillance', 'code':'surveillance'})
        }
    })
    subscription_coordinator.device_repository.load({
        'default' : {
            '001': Device(**{'id':'001', 'name':'Android SSX10', 'locator':'ABC123'})
        }
    })
    return subscription_coordinator


def test_subscription_coordinator_instantiation(subscription_coordinator):
    assert subscription_coordinator is not None

def test_channel_coordinator_create_channel(subscription_coordinator):
    channel_dict = {'name': 'Channel 2', 'code': 'CH002'}
    subscription_coordinator.create_channel(channel_dict)

# def test_get_channels(subscription_coordinator):
#     channel_dict = {'id': '001', 'name': 'Channel 1', 'code': 'CH001'}
#     subscription_coordinator.get_channels(channel_dict['id'])
#     assert len(subscription_coordinator.channel_repository.items) > 0


def test_subscription_coordinator_subscribe(subscription_coordinator):
    subscription_dict = {'device_id': '001', 'channel_id': '001'}
    subscription_coordinator.subscribe(subscription_dict)
    assert len(subscription_coordinator.device_channel_repository.data) == 1


# def test_subscription_coordinator_subscribe_delivery_service(
#         subscription_coordinator):
#     code = 'surveillance'
#     locator = 'ABC123'
#     subscription_dict = {'device_id': '001', 'channel_id': '001'}
#     subscription_coordinator.subscribe(subscription_dict)

#     assert subscription_coordinator.delivery_service.code == code
#     assert subscription_coordinator.delivery_service.locator == locator
