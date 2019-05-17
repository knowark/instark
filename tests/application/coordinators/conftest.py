from pytest import fixture
from instark.application.repositories import (
    MemoryDeviceRepository, MemoryChannelRepository,
    MemorySubscriptionRepository, MemoryMessageRepository)
from instark.application.utilities.query_parser import QueryParser
from instark.application.services import (
    StandardIdService, MemoryDeliveryService)


@fixture
def id_service():
    return StandardIdService()


@fixture
def device_repository():
    return MemoryDeviceRepository(QueryParser())


@fixture
def channel_repository():
    return MemoryChannelRepository(QueryParser())


@fixture
def device_channel_repository():
    return MemorySubscriptionRepository(QueryParser())


@fixture
def message_repository():
    return MemoryMessageRepository(QueryParser())


@fixture
def delivery_service():
    return MemoryDeliveryService()
