from pytest import fixture
from instark.application.models import Message


@fixture
def message():
    return Message()


def test_message_instantiation(message):
    assert message is not None
