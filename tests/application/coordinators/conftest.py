from pytest import fixture
from instark.application.repositories import (
    ExpressionParser, MemoryDeviceRepository, MemoryChannelRepository,
    MemoryDeviceChannelRepository, MemoryMessageRepository)
from instark.application.services import (
    StandardIdService, MemoryDeliveryService)


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


@fixture
def message_repository():
    return MemoryMessageRepository(ExpressionParser())


@fixture
def delivery_service():
    return MemoryDeliveryService()
