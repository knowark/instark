from pytest import fixture
from instark.application.coordinators import RegistrationCoordinator


@fixture
def registration_coordinator(id_service, device_repository):
    return RegistrationCoordinator(id_service, device_repository)


def test_registation_coordinator_instantiation(registration_coordinator):
    assert registration_coordinator is not None


def test_registation_coordinator_register_device(registration_coordinator):
    registration_dict = {'name': 'DEV001', 'locator': 'a1b2c3d4'}
    registration_coordinator.register_device(registration_dict)

    assert len(registration_coordinator.device_repository.items) == 1
