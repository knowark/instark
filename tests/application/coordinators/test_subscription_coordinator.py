from pytest import fixture
from instark.application.coordinators import SubscriptionCoordinator


@fixture
def subscription_coordinator(id_service, channel_repository,
                             device_channel_repository):
    return SubscriptionCoordinator(id_service, channel_repository,
                                   device_channel_repository)


def test_subscription_coordinator_instantiation(subscription_coordinator):
    assert subscription_coordinator is not None


def test_channel_coordinator_create_channel(subscription_coordinator):
    channel_dict = {'name': 'Channel 1', 'code': 'CH001'}
    subscription_coordinator.create_channel(channel_dict)

    assert len(subscription_coordinator.channel_repository.items) == 1


def test_subscription_coordinator_subscribe(subscription_coordinator):
    subscription_dict = {'device_id': '001', 'channel_id': '001'}
    subscription_coordinator.subscribe(subscription_dict)

    assert len(subscription_coordinator.device_channel_repository.items) == 1
