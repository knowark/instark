from pytest import fixture, raises
from instark.application.models import Device, Channel
from instark.application.coordinators import NotificationCoordinator
from instark.application.repositories import (
    MemoryChannelRepository, MemoryDeviceRepository,
    MemorySubscriptionRepository, MemoryMessageRepository)
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

def message_repository() -> MemoryMessageRepository:
    tenant_provider = StandardTenantProvider(Tenant(name="Default"))
    parser = QueryParser()
    message_repository = MemoryMessageRepository(parser, tenant_provider)
    return message_repository

@fixture
def notification_coordinator(id_service, channel_repository, device_repository,
                             message_repository, delivery_service):
    return NotificationCoordinator(id_service, channel_repository,
                                   device_repository, message_repository,
                                   delivery_service)

def test_notification_coordinator_instantiation(notification_coordinator):
    assert notification_coordinator is not None

def test_notification_coordinator_send_direct_message(
        notification_coordinator):
    notification_coordinator.delivery_service.response = 'a1b2c3'
    notification_coordinator.device_repository.load(
        Device(**{'id':'1', 'name':'Device 1', 'locator':'ABC123'})
    )
    message_dict = {
        'recipient_id': '1',
        'kind': 'direct',
        'content': 'Hello',
        'title': 'Tittle notification'
    }
    # notification_coordinator.send_message(message_dict)

#     assert len(notification_coordinator.message_repository.items) == 1


def test_notification_coordinator_send_direct_message_failed(
        notification_coordinator):
    notification_coordinator.device_repository.load({
        'default' : {
            '1': Device(**{'id':'1', 'name':'Device 1', 'locator':'ABC123'})
        }
    })
    message_dict = {
        'recipient_id': '1', 'kind': 'Direct', 'content': 'Hello'}
    notification_coordinator.delivery_service.response = ''

    with raises(ValueError):
        notification_coordinator.send_message(message_dict)


def test_notification_coordinator_send_channel_message(
        notification_coordinator):
    notification_coordinator.delivery_service.response = 'BROADCAST'
    notification_coordinator.channel_repository.load({
        'default' : {
            '1': Channel(**{'id':'1', 'name':'Channel XYZ', 'code':'news'})
        }
    })
    message_dict = {
        'recipient_id': '1', 'kind': 'Channel', 'content': 'Hello'}

    # notification_coordinator.send_message(message_dict)

#     assert len(notification_coordinator.message_repository.items) == 1

#     for id, message in (
#             notification_coordinator.message_repository.items.items()):
#         assert message.recipient_id == '1'
#         assert message.kind == 'Channel'
