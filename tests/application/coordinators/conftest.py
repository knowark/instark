from pytest import fixture
from instark.application.repositories import (
    ExpressionParser, MemoryDeviceRepository, MemoryChannelRepository,
    MemoryDeviceChannelRepository)
from instark.application.services import StandardIdService


@fixture
def id_service():
    return StandardIdService()


@fixture
def device_repository():
    return MemoryDeviceRepository(ExpressionParser())


@fixture
def channel_repository():
    return MemoryChannelRepository(ExpressionParser())


@fixture
def device_channel_repository():
    return MemoryDeviceChannelRepository(ExpressionParser())
