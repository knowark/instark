from pytest import fixture
from instark.application.repositories import (
    MemoryDeviceRepository, MemoryChannelRepository,
    MemorySubscriptionRepository, MemoryMessageRepository)
from instark.application.utilities.query_parser import QueryParser
from instark.application.services import (
    StandardIdService, MemoryDeliveryService)
from instark.application.utilities.tenancy import TenantProvider, Tenant



@fixture
def id_service():
    return StandardIdService()


@fixture
def device_repository():
    return MemoryDeviceRepository(QueryParser(), TenantProvider)


@fixture
def channel_repository():
    return MemoryChannelRepository(QueryParser(), TenantProvider)


@fixture
def device_channel_repository():
    return MemorySubscriptionRepository(QueryParser(), TenantProvider)


@fixture
def message_repository():
    return MemoryMessageRepository(QueryParser(), TenantProvider)


@fixture
def delivery_service():
    return MemoryDeliveryService()
