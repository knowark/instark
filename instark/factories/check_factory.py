from injectark import Factory
from ..application.domain.common import (
    User, Tenant, QueryParser,
    TenantProvider, StandardTenantProvider,
    AuthProvider, StandardAuthProvider)
from ..application.domain.models import Device, Channel, Message, Subscription
from ..application.domain.repositories import (
    MemoryChannelRepository, MemoryDeviceRepository,
    MemorySubscriptionRepository, MemoryMessageRepository)
from .base_factory import BaseFactory
from ..core import (
    Config, MemoryTenantSupplier)


class CheckFactory(BaseFactory):
    def __init__(self, config: Config) -> None:
        super().__init__(config)
        self.config = config

    # Tenancy

    def check_tenant_provider(self) -> StandardTenantProvider:
        tenant_provider = StandardTenantProvider()
        tenant_provider.setup(Tenant(name="Default"))
        return tenant_provider

    def check_auth_provider(self) -> StandardAuthProvider:
        auth_provider = StandardAuthProvider()
        auth_provider.setup(User(id='001', name='johndoe'))
        return auth_provider

    def memory_channel_repository(
        self, query_parser: QueryParser,
        tenant_provider: TenantProvider,
        auth_provider: AuthProvider
    ) -> MemoryChannelRepository:
        channel_repository = MemoryChannelRepository(
            query_parser, tenant_provider, auth_provider)
        channel_repository.load({
            'default': {
                '001': Channel(id='001', name='Channel 1', code='CH001'),
                '002': Channel(id='002', name='Channel 2', code='CH002'),
                '003': Channel(id='003', name='Channel 3', code='CH003')

            }
        })
        return channel_repository

    def memory_device_repository(
        self, query_parser: QueryParser,
        tenant_provider: TenantProvider,
        auth_provider: AuthProvider
    ) -> MemoryDeviceRepository:
        device_repository = MemoryDeviceRepository(
            query_parser, tenant_provider, auth_provider)
        device_repository.load({
            'default': {
                '001': Device(
                    **{'id': '001', 'name': 'DEV001', 'locator': '1'}),
                '002': Device(
                    **{'id': '002', 'name': 'DEV002', 'locator': '2'})
            }
        })
        return device_repository

    def memory_message_repository(
        self, query_parser: QueryParser,
        tenant_provider: TenantProvider,
        auth_provider: AuthProvider
    ) -> MemoryMessageRepository:
        message_repository = MemoryMessageRepository(
            query_parser, tenant_provider, auth_provider)
        message_repository.load({
            'default': {
                '001': Message(id='001', recipient_id='001', kind='direct',
                               content='Super!', title='Hello')
            }
        })
        return message_repository

    def memory_subscription_repository(
        self, query_parser: QueryParser,
        tenant_provider: TenantProvider,
        auth_provider: AuthProvider
    ) -> MemorySubscriptionRepository:
        subscription_repository = MemorySubscriptionRepository(
            query_parser, tenant_provider, auth_provider)
        subscription_repository.load({
            'default': {
                '001': Subscription(**{'id': '001', 'device_id': '001',
                                       'channel_id': '001'}),
                '002': Subscription(**{'id': '001', 'device_id': '002',
                                       'channel_id': '001'})
            }
        })
        return subscription_repository

    def check_tenant_supplier(self) -> MemoryTenantSupplier:
        tenant_supplier = MemoryTenantSupplier()
        tenant_supplier.ensure_tenant({
            'id': '001',
            'name': 'Default',
            'zone': 'default',
            'data': {
                'memory': {
                    'default': 'default'
                }
            }})
        return tenant_supplier
