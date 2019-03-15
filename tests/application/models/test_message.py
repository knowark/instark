from pytest import fixture
from instark.application.models import Message


@fixture
def message():
    return Message(
        id='1',
        recipient_id='3',
        kind='Direct',
        content='Hello World',
        subject='Message Direct of admin'
    )


def test_message_instantiation(message):
    assert message is not None


def test_message_attributes(message):
    assert message.recipient_id == '3'
    assert message.kind == 'Direct'
    assert message.backend_id == ''
    assert message.content == 'Hello World'
    assert message.subject == 'Message Direct of admin'
