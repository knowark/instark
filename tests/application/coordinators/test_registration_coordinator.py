from pytest import fixture
from instark.application.coordinators import RegistrationCoordinator
from instark.application.repositories import (MemoryDeviceRepository)
from instark.application.utilities import (
    QueryParser, StandardTenantProvider, Tenant)


@fixture
def registration_coordinator(device_repository):
    return RegistrationCoordinator(device_repository)


def test_registation_coordinator_instantiation(
        registration_coordinator: RegistrationCoordinator) -> None:
    assert registration_coordinator is not None


async def test_registation_coordinator_register_device(
        registration_coordinator: RegistrationCoordinator) -> None:
    registration_dicts: RecordList = [{
        'name': 'DEV001',
        'locator': 'a1b2c3d4'
    }]
    await registration_coordinator.register_device(registration_dicts)

    assert len(registration_coordinator.device_repository.data) == 1


async def test_registration_coordinator_delete_device(
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
