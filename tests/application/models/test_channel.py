from pytest import fixture
from instark.application.models import Channel


@fixture
def channel():
    return Channel()


def test_channel_instantiation(channel):
    assert channel is not None
