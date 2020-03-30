from pytest import fixture
from instark.application.coordinators import RegistrationCoordinator
from instark.application.repositories import (MemoryDeviceRepository)
from instark.application.utilities import (
    QueryParser, StandardTenantProvider, Tenant)


@fixture
def registration_coordinator(device_repository):
    return RegistrationCoordinator(device_repository)


def test_registation_coordinator_instantiation(registration_coordinator):
    assert registration_coordinator is not None


async def test_registation_coordinator_register_device(registration_coordinator):
    registration_dicts : RecordList = [{
        'name': 'DEV001', 
        'locator': 'a1b2c3d4'
    }]
    await registration_coordinator.register_device(registration_dicts)

    assert len(registration_coordinator.device_repository.data) == 1
