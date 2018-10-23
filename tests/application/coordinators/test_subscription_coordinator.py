from pytest import fixture
from instark.application.coordinators import SubscriptionCoordinator


@fixture
def subscription_coordinator(id_service, device_repository):
    return SubscriptionCoordinator(id_service, device_repository)


def test_subscription_coordinator_instantiation(subscription_coordinator):
    assert subscription_coordinator is not None


def test_channel_coordinator_create_channel(subscription_coordinator):
    channel_dict = {'name': 'Channel 1', 'code': 'CH001'}
    subscription_coordinator.create_channel(channel_dict)

    assert len(subscription_coordinator.channel_repository.items) == 1
