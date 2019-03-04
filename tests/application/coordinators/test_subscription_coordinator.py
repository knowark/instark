from pytest import fixture
from instark.application.models import Device, Channel
from instark.application.coordinators import SubscriptionCoordinator


@fixture
def subscription_coordinator(id_service, channel_repository,
                             device_repository, device_channel_repository,
                             delivery_service):
    subscription_coordinator = SubscriptionCoordinator(
        id_service, channel_repository, device_repository,
        device_channel_repository, delivery_service)
    subscription_coordinator.channel_repository.load({
        '001': Channel(id='001', name='Surveillance', code='surveillance')
    })
    subscription_coordinator.device_repository.load({
        '001': Device(id='001', name='Android SSX10', locator='ABC123')
    })
    return subscription_coordinator


def test_subscription_coordinator_instantiation(subscription_coordinator):
    assert subscription_coordinator is not None


def test_channel_coordinator_create_channel(subscription_coordinator):
    channel_dict = {'name': 'Channel 1', 'code': 'CH001'}
    subscription_coordinator.create_channel(channel_dict)

    assert len(subscription_coordinator.channel_repository.items) == 2


def test_subscription_coordinator_subscribe(subscription_coordinator):
    subscription_dict = {'device_id': '001', 'channel_id': '001'}
    subscription_coordinator.subscribe(subscription_dict)

    assert len(subscription_coordinator.device_channel_repository.items) == 1


def test_subscription_coordinator_subscribe_delivery_service(
        subscription_coordinator):
    code = 'surveillance'
    locator = 'ABC123'
    subscription_dict = {'device_id': '001', 'channel_id': '001'}
    subscription_coordinator.subscribe(subscription_dict)

    assert subscription_coordinator.delivery_service.code == code
    assert subscription_coordinator.delivery_service.locator == locator
