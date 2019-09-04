from pytest import fixture
from instark.application.repositories import (
    MemoryDeviceRepository, MemoryChannelRepository,
    MemorySubscriptionRepository, MemoryMessageRepository)
from instark.application.utilities.query_parser import QueryParser
from instark.application.services import (
    StandardIdService, MemoryDeliveryService)
from instark.application.utilities.tenancy import (
    StandardTenantProvider, Tenant)


@fixture
def id_service():
    return StandardIdService()


@fixture
def tenant_provider():
    return StandardTenantProvider(Tenant(name="default"))


@fixture
def device_repository(tenant_provider):
    return MemoryDeviceRepository(QueryParser(), tenant_provider)


@fixture
def channel_repository(tenant_provider):
    return MemoryChannelRepository(QueryParser(), tenant_provider)


@fixture
def device_channel_repository(tenant_provider):
    return MemorySubscriptionRepository(QueryParser(), tenant_provider)


@fixture
def message_repository(tenant_provider):
    return MemoryMessageRepository(QueryParser(), tenant_provider)


@fixture
def delivery_service(tenant_provider):
    return MemoryDeliveryService(tenant_provider)
