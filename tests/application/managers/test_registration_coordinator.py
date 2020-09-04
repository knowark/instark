from pytest import fixture
from instark.application.domain.models import Device, Message, Subscription
from instark.application.managers import RegistrationManager
from instark.application.domain.common import RecordList
from instark.application.domain.repositories import (
    MemoryDeviceRepository, MemoryMessageRepository,
    MemorySubscriptionRepository)
from instark.application.domain.common import (
    QueryParser, StandardTenantProvider, Tenant)


@fixture
def registration_manager(device_repository, message_repository,
                         subscription_repository, delivery_service):
    registration_manager = RegistrationManager(
        device_repository, message_repository,
        subscription_repository, delivery_service)
    return registration_manager


def test_registation_manager_instantiation(
        registration_manager: RegistrationManager) -> None:
    assert registration_manager is not None


async def test_registation_manager_register_device(
        registration_manager: RegistrationManager) -> None:
    registration_dicts: RecordList = [{
        'name': 'DEV001',
        'locator': 'abcd1234'
    }]
    await registration_manager.register_device(registration_dicts)


async def test_subscription_manager_delete_device_with_message(
        registration_manager: RegistrationManager) -> None:
    device_id = '07506ce5-edd7-4eab-af9c-4e555bc8e098'
    device_records: RecordList = [{
        'id': device_id,
        'name': 'DEV003',
        'locator': '1234abcd'
    }]

    await registration_manager.register_device(device_records)

    registration_manager.message_repository.load({
        'default': {
            '001': Message(id='001',
                           recipient_id=device_id,
                           content='Hello world',
                           kind='direct')
        }
    })

    devices_data = getattr(
        registration_manager.device_repository, 'data')

    assert len(devices_data['default']) == 1
    result = await registration_manager.delete_device([device_id])


async def test_registration_manager_delete_device_without_messsage(
        registration_manager: RegistrationManager) -> None:
    device_id = '07506ce5-edd7-4eab-af9c-4e555bc8e098'
    device_records: RecordList = [{
        'id': device_id,
        'name': 'device 3',
        'code': 'CH003'
    }]
    await registration_manager.register_device(device_records)
    devices_data = getattr(
        registration_manager.device_repository, 'data')
    assert len(devices_data['default']) == 1
    await registration_manager.delete_device([device_id])
    assert len(devices_data['default']) == 0


async def test_subscription_manager_delete_device_without_ids(
        registration_manager: RegistrationManager) -> None:
    device_id = ''
    await registration_manager.delete_device([device_id])
