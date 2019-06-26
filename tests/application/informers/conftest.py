from pytest import fixture
from instark.application.models import Device, Channel, Message, Subscription
from instark.application.repositories import (
    DeviceRepository, MemoryDeviceRepository,
    MessageRepository, MemoryMessageRepository,
    SubscriptionRepository, MemorySubscriptionRepository)
from instark.application.utilities.query_parser import QueryParser
from instark.application.utilities.tenancy import Tenant, StandardTenantProvider
from instark.application.informers.instark_informer import InstarkInformer
from instark.application.informers.standard_instark_informer import StandardInstarkInformer


@fixture
def device_repository() -> DeviceRepository:
    parser = QueryParser()
    tenant_service = StandardTenantProvider(Tenant(name="Default"))
    device_repository = MemoryDeviceRepository(parser, tenant_service)
    device_repository.load({
        'default': {
            '001': Device(**{'id':'001', 'name':'DEV001', 'locator':'1'}),
            '002': Device(**{'id':'002', 'name':'DEV002', 'locator':'2'})
        }
    })
    return device_repository


@fixture
def channel_repository():
    parser = QueryParser()
    tenant_service = StandardTenantProvider(Tenant(name="Default"))
    channel_repository = MemoryDeviceRepository(parser, tenant_service)
    channel_repository.load({
        'default' : {
            '001': Channel(**{'id':'001', 'name':'Channel 1', 'code':'CH001'}),
            '002': Channel(**{'id':'002', 'name':'Channel 2', 'code':'CH002'}),
            '003': Channel(**{'id':'003', 'name':'Channel 3', 'code':'CH003'})
        }    
    })
    return channel_repository


@fixture
def message_repository():
    parser = QueryParser()
    tenant_service = StandardTenantProvider(Tenant(name="Default"))
    message_repository = MemoryMessageRepository(parser, tenant_service)
    message_repository.load({
        'default' : {
            '001': Message(** {'id':'001', 'recipient_id':'001', 'kind':'direct',
                        'content':'Super!', 'title': 'Hello'})
        }
    })
    return message_repository


@fixture
def device_channel_repository():
    parser = QueryParser()
    tenant_service = StandardTenantProvider(Tenant(name="Default"))
    device_channel_repository = MemorySubscriptionRepository(parser, tenant_service)
    device_channel_repository.load({
        'default' : {
            '001': Subscription(**{'id':'001', 'device_id':'001',
                                'channel_id':'001'}),
            '002': Subscription(**{'id':'001', 'device_id':'002',
                                'channel_id':'001'})
        }    
    })
    return device_channel_repository


@fixture
def instark_informer(device_repository, channel_repository,
                     message_repository, device_channel_repository):
    return StandardInstarkInformer(
        device_repository, channel_repository,
        message_repository, device_channel_repository)
