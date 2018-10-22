from pytest import fixture
from instark.application.coordinators import RegistrationCoordinator


@fixture
def registration_coordinator():
    return RegistrationCoordinator()


def test_registation_coordinator_instantiation(registration_coordinator):
    assert registration_coordinator is not None
