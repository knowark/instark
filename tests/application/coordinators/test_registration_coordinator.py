from pytest import fixture
from instark.application.models import Device, Message, Subscription
from instark.application.coordinators import RegistrationCoordinator
from instark.application.repositories import (
    MemoryDeviceRepository, MemoryMessageRepository,
    MemorySubscriptionRepository)
from instark.application.utilities import (
    QueryParser, StandardTenantProvider, Tenant)


@fixture
def registration_coordinator(device_repository, message_repository,
                             subscription_repository, delivery_service):
    registration_coordinator = RegistrationCoordinator(
        device_repository, message_repository,
        subscription_repository, delivery_service)
    return registration_coordinator


def test_registation_coordinator_instantiation(
        registration_coordinator: RegistrationCoordinator) -> None:
    assert registration_coordinator is not None


async def test_registation_coordinator_register_device(
        registration_coordinator: RegistrationCoordinator) -> None:
    registration_dicts: RecordList = [{
        'name': 'DEV001',
        'locator': 'abcd1234'
    }]
    await registration_coordinator.register_device(registration_dicts)


async def test_subscription_coordinator_delete_device_with_message(
        registration_coordinator: RegistrationCoordinator) -> None:
    device_id = '07506ce5-edd7-4eab-af9c-4e555bc8e098'
    device_records: RecordList = [{
        'id': device_id,
        'name': 'DEV003',
        'locator': '1234abcd'
    }]

    await registration_coordinator.register_device(device_records)

    registration_coordinator.message_repository.load({
        'default': {
            '001': Message(id='001',
                           recipient_id=device_id,
                           content='Hello world',
                           kind='direct')
        }
    })

    devices_data = getattr(
        registration_coordinator.device_repository, 'data')

    print("devices data test subs regis coord    ", devices_data)

    assert len(devices_data['default']) == 1
    result = await registration_coordinator.delete_device([device_id])


async def test_registration_coordinator_delete_device_without_messsage(
        registration_coordinator: RegistrationCoordinator) -> None:
    device_id = '07506ce5-edd7-4eab-af9c-4e555bc8e098'
    device_records: RecordList = [{
        'id': device_id,
        'name': 'device 3',
        'code': 'CH003'
    }]
    await registration_coordinator.register_device(device_records)
    devices_data = getattr(
        registration_coordinator.device_repository, 'data')
    print("data en test subs:  ", devices_data)
    assert len(devices_data['default']) == 1
    await registration_coordinator.delete_device([device_id])
    assert len(devices_data['default']) == 0

async def test_subscription_coordinator_delete_device_without_ids(
        registration_coordinator: RegistrationCoordinator) -> None:
    device_id = ''
    await registration_coordinator.delete_device([device_id])