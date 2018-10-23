from pytest import fixture
from instark.application.models import DeviceChannel


@fixture
def device_channel():
    return DeviceChannel(
        id='001',
        device_id='001',
        channel_id='001'
    )


def test_device_channel_instantiation(device_channel):
    assert device_channel is not None


def test_device_channel_attributes(device_channel):
    assert device_channel.device_id == '001'
    assert device_channel.channel_id == '001'
