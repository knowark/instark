from ..configuration import Config
from ...application.utilities import (
    QueryParser, Tenant, TenantProvider, StandardTenantProvider)
from ...application.services import AuthService, StandardAuthService
from ...application.models import (
    channel, device, message, subscription)  
from ...application.repositories import (
    MemoryChannelRepository, MemoryDeviceRepository,
    MemorySubscriptionRepository, MemoryMessageRepository)
from .memory_factory import MemoryFactory
from ...infrastructure.core import (
    TenantSupplier, MemoryTenantSupplier)


class TrialFactory(MemoryFactory):
    def __init__(self, config: Config) -> None:
        self.config = config

    # Tenancy

    def trial_tenant_provider(self) -> StandardTenantProvider:
        tenant_provider = StandardTenantProvider()
        tenant_provider.setup(Tenant(name="Default"))
        return tenant_provider

    def trial_auth_service(self) -> StandardAuthService:
        auth_service = StandardAuthService()
        auth_service.setup(User(id='001', name='johndoe'))
        return auth_service

    def memory_channel_repository(
        self, query_parser: QueryParser,
        tenant_provider: TenantProvider,
        auth_service: AuthService
    ) -> MemoryChannelRepository:
        channel_repository = MemoryChannelRepository(
            query_parser, tenant_provider, auth_service)
        """channel_repository.load({
            "default": {
                'LMK123': channel(
                    **{'id': 'LMK123', 'name': 'General Survey'}),
                'QWT987': channel(
                    **{'id': 'QWT987', 'name': 'Surveillance'}),
                'HJK456': channel(
                    **{'id': 'HJK456', 'name': 'Inspections'})
            }
        })"""
        return channel_repository

    def memory_device_repository(
        self, query_parser: QueryParser,
        tenant_provider: TenantProvider,
        auth_service: AuthService
    ) -> MemoryDeviceRepository:
        device_repository = MemoryDeviceRepository(
            query_parser, tenant_provider, auth_service)
        """device_repository.load({
            "default": {
                '001': device(
                    **{'id': '001', 'name': 'Are alarms working?',
                       'type': 'selection', 'channel_id': 'LMK123'}),
            }
        })"""
        return device_repository

    def memory_message_repository(
        self, query_parser: QueryParser,
        tenant_provider: TenantProvider,
        auth_service: AuthService
    ) -> MemoryMessageRepository:
        message_repository = MemoryMessageRepository(
            query_parser, tenant_provider, auth_service)
        """message_repository.load({
            "default": {
                'ABC': message(
                    **{'id': 'ABC', 'name': 'Yes',
                       'device_id': 'ABC'}),
            }
        })"""
        return message_repository

    def memory_subscription_repository(
        self, query_parser: QueryParser,
        tenant_provider: TenantProvider,
        auth_service: AuthService
    ) -> MemorySubscriptionRepository:
        subscription_repository = MemorySubscriptionRepository(
            query_parser, tenant_provider, auth_service)
        """subscription_repository.load({
            "default": {
                '001': subscription(
                    **{'id': '001', 'name': 'General Survey subscription',
                       'channel_id': 'LMK123'}),
                '002': subscription(
                    **{'id': '002', 'name': 'General Survey subscription',
                       'channel_id': 'LMK123'}),
            }
        })"""
        return subscription_repository

    def trial_tenant_supplier(self) -> MemoryTenantSupplier:
        tenant_supplier = MemoryTenantSupplier()
        tenant_supplier.create_tenant({
            'id': '001',
            'name': 'Default',
            'zone': 'default',
            'data': {
                'memory': {
                    'default': 'default'
                }
            }})
        return tenant_supplier

