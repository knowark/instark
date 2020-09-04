from pytest import fixture
from instark.application.domain.models import Device


@fixture
def device():
    return Device(
        id='1',
        name='DEV001',
        locator='a1b2c3d4'
    )


def test_device_instantiation(device):
    assert device is not None


def test_device_attributes(device):
    assert device.name == 'DEV001'
    assert device.locator == 'a1b2c3d4'
