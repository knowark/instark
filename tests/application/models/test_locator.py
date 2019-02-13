from pytest import fixture
from instark.application.models import Locator


@fixture
def locator():
    return Locator(
        id='1',
        medium='http',
        type='device',
        reference_id=''
    )


def test_locator_instantiation(locator):
    assert locator is not None


def test_locator_attributes(locator):
    assert locator.medium == 'http'
    assert locator.type == 'device'
    assert locator.reference_id == ''
