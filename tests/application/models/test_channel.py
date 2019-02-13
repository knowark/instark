from pytest import fixture
from instark.application.models import Channel


@fixture
def channel():
    return Channel(
        id='001',
        name='Channel 1',
        code='CH001',
        locator_id='1'
    )


def test_channel_instantiation(channel):
    assert channel is not None


def test_channel_attributes(channel):
    assert channel.name == 'Channel 1'
    assert channel.code == 'CH001'
    assert channel.locator_id == '1'
