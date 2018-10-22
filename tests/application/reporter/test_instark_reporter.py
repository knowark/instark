from pytest import fixture
from instark.application.models import Device
from instark.application.repositories import (
    ExpressionParser, MemoryDeviceRepository)
from instark.application.reporters import (
    InstarkReporter, MemoryInstarkReporter)


@fixture
def device_repository():
    parser = ExpressionParser()
    device_repository = MemoryDeviceRepository(parser)
    device_repository.load({
        '001': Device(id='001', name='DEV001', locator='a1b2c3'),
        '002': Device(id='002', name='DEV002', locator='x1y2z3')
    })
    return device_repository


@fixture
def instark_reporter(device_repository):
    return MemoryInstarkReporter(device_repository)


def test_instark_reporter_instantiation(instark_reporter):
    assert isinstance(instark_reporter, InstarkReporter)


def test_instark_reporter_search_devices(instark_reporter):
    result = instark_reporter.search_devices([])
    assert len(result) == 2
