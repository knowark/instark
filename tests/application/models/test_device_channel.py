from pytest import fixture
from instark.application.models import DeviceChannel


@fixture
def device_channel():
    return DeviceChannel()


def test_device_channel_instantiation(device_channel):
    assert device_channel is not None
