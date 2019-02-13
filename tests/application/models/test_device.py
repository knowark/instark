from pytest import fixture
from instark.application.models import Device


@fixture
def device():
    return Device(
        id='1',
        name='DEV001',
        locator_id='1'
    )


def test_device_instantiation(device):
    assert device is not None


def test_device_attributes(device):
    assert device.name == 'DEV001'
    assert device.locator_id == '1'
