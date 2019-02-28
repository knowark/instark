from pytest import fixture
from instark.application.repositories import (
    ExpressionParser, MemoryDeviceRepository, MemoryChannelRepository,
    MemorySubscriptionRepository, MemoryMessageRepository,
    MemoryLocatorRepository)
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
def locator_repository():
    return MemoryLocatorRepository(ExpressionParser())


@fixture
def device_channel_repository():
    return MemorySubscriptionRepository(ExpressionParser())


@fixture
def message_repository():
    return MemoryMessageRepository(ExpressionParser())


@fixture
def delivery_service():
    return MemoryDeliveryService()
