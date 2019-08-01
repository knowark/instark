from pytest import fixture
from instark.application.coordinators import RegistrationCoordinator
from instark.application.repositories import (MemoryDeviceRepository)
from instark.application.utilities import (
    QueryParser, StandardTenantProvider, Tenant)

@fixture
def device_repository() -> MemoryDeviceRepository:
    tenant_provider = StandardTenantProvider(Tenant(name="Default"))
    parser = QueryParser()
    device_repository = MemoryDeviceRepository(parser, tenant_provider)
    return device_repository

@fixture
def registration_coordinator(id_service, device_repository):
    return RegistrationCoordinator(id_service, device_repository)


def test_registation_coordinator_instantiation(registration_coordinator):
    assert registration_coordinator is not None


def test_registation_coordinator_register_device(registration_coordinator):
    registration_dict = {'name': 'DEV001', 'locator': 'a1b2c3d4'}
    registration_coordinator.register_device(registration_dict)

    assert len(registration_coordinator.device_repository.data) == 1
