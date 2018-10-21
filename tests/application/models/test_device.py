from pytest import fixture
from instark.application.models import Device


@fixture
def device():
    return Device()


def test_device_instantiation(device):
    assert device is not None
