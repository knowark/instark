from pytest import fixture, raises
from instark.application.models import Device
from instark.application.coordinators import NotificationCoordinator


@fixture
def notification_coordinator(id_service, device_repository,
                             message_repository, delivery_service):
    return NotificationCoordinator(id_service, device_repository,
                                   message_repository, delivery_service)


def test_notification_coordinator_instantiation(notification_coordinator):
    assert notification_coordinator is not None


def test_notification_coordinator_send_direct_message(
        notification_coordinator):
    notification_coordinator.device_repository.load(
        {'1': Device(id='1', name='Device 1', locator='ABC123')})
    message_dict = {
        'recipient_id': '1', 'kind': 'Direct', 'content': 'Hello'}

    result = notification_coordinator.send_direct_message(message_dict)

    assert len(notification_coordinator.message_repository.items) == 1


def test_notification_coordinator_send_direct_message_failed(
        notification_coordinator):
    notification_coordinator.device_repository.load(
        {'1': Device(id='1', name='Device 1', locator='ABC123')})
    message_dict = {
        'recipient_id': '1', 'kind': 'Direct', 'content': 'Hello'}
    notification_coordinator.delivery_service.sent = False

    with raises(ValueError):
        notification_coordinator.send_direct_message(message_dict)