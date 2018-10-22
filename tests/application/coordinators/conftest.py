from pytest import fixture
from instark.application.repositories import (
    ExpressionParser, DeviceRepository, MemoryDeviceRepository)
from instark.application.services import StandardIdService


@fixture
def id_service():
    return StandardIdService()


@fixture
def device_repository():
    return MemoryDeviceRepository(ExpressionParser())
