from pytest import fixture
from instark.application.repositories import (
    ExpressionParser, MemoryDeviceRepository)
from instark.application.reporters import (
    InstarkReporter, MemoryInstarkReporter)


@fixture
def instark_reporter():
    parser = ExpressionParser()
    device_repository = MemoryDeviceRepository(parser)
    return MemoryInstarkReporter(device_repository)


def test_instark_reporter_instantiation(instark_reporter):
    assert isinstance(instark_reporter, InstarkReporter)
