from injectark import Factory
from ..application.domain.common import (
    Tenant, QueryParser, TenantProvider, StandardTenantProvider,
    AuthProvider, StandardAuthProvider,
    TransactionManager, MemoryTransactionManager)
from ..application.domain.repositories import (
    DeviceRepository, MemoryDeviceRepository,
    ChannelRepository, MemoryChannelRepository,
    SubscriptionRepository, MemorySubscriptionRepository,
    MessageRepository, MemoryMessageRepository)
from ..application.domain.services import (MemoryDeliveryService,
                                           DeliveryService)
from ..application.managers import (
    NotificationManager, RegistrationManager, SessionManager,
    SubscriptionManager)
from ..application.informers import StandardInstarkInformer
from ..core import (
    Config, MemoryTenantSupplier, MemoryMigrationSupplier)


class BaseFactory(Factory):
    def __init__(self, config: Config) -> None:
        self.config = config

     # Providers

    def query_parser(self) -> QueryParser:
        return QueryParser()

    def standard_tenant_provider(self) -> StandardTenantProvider:
        return StandardTenantProvider()

    def standard_auth_provider(self) -> StandardAuthProvider:
        return StandardAuthProvider()

    def memory_transaction_manager(self) -> MemoryTransactionManager:
        return MemoryTransactionManager()

    # Repositories

    def memory_device_repository(
        self, query_parser: QueryParser,
        tenant_provider: TenantProvider,
        auth_provider: AuthProvider
    ) -> MemoryDeviceRepository:
        return MemoryDeviceRepository(
            query_parser, tenant_provider, auth_provider)

    def memory_channel_repository(
        self, query_parser: QueryParser,
        tenant_provider: TenantProvider,
        auth_provider: AuthProvider
    ) -> MemoryChannelRepository:
        return MemoryChannelRepository(
            query_parser, tenant_provider, auth_provider)

    def memory_subscription_repository(
        self, query_parser: QueryParser,
        tenant_provider: TenantProvider,
        auth_provider: AuthProvider
    ) -> MemorySubscriptionRepository:
        return MemorySubscriptionRepository(
            query_parser, tenant_provider, auth_provider)

    def memory_message_repository(
        self, query_parser: QueryParser,
        tenant_provider: TenantProvider,
        auth_provider: AuthProvider
    ) -> MemoryMessageRepository:
        return MemoryMessageRepository(
            query_parser, tenant_provider, auth_provider)

    # Services

    def memory_delivery_service(self) -> MemoryDeliveryService:
        return MemoryDeliveryService('Fake Response')

    # Managers

    def registration_manager(
        self, device_repository: DeviceRepository,
        message_repository: MessageRepository,
        subscription_manager: SubscriptionRepository,
        transaction_manager: TransactionManager,
        delivery_service: DeliveryService
    ) -> RegistrationManager:
        return transaction_manager(RegistrationManager)(
            device_repository, message_repository, subscription_manager,
            delivery_service)

    def subscription_manager(
        self, channel_repository: ChannelRepository,
        device_repository: DeviceRepository,
        message_repository: MessageRepository,
        subscription_repository: SubscriptionRepository,
        delivery_service: DeliveryService,
        transaction_manager: TransactionManager
    ) -> SubscriptionManager:
        return transaction_manager(SubscriptionManager)(
            channel_repository, device_repository, message_repository,
            subscription_repository,
            delivery_service)

    def notification_manager(
        self, channel_repository: ChannelRepository,
        device_repository: DeviceRepository,
        message_repository: MessageRepository,
        delivery_service: DeliveryService,
        transaction_manager: TransactionManager
    ) -> NotificationManager:
        return transaction_manager(NotificationManager)(
            channel_repository,
            device_repository, message_repository, delivery_service)

    def session_manager(
        self, tenant_provider: TenantProvider,
        auth_provider: AuthProvider
    ) -> SessionManager:
        return SessionManager(tenant_provider, auth_provider)

    # Informers

    def standard_instark_informer(
        self, device_repository: DeviceRepository,
        channel_repository: ChannelRepository,
        message_repository: MessageRepository,
        subscription_repository: SubscriptionRepository,
        transaction_manager: TransactionManager
    ) -> StandardInstarkInformer:
        return transaction_manager(StandardInstarkInformer)(
            device_repository, channel_repository,
            message_repository, subscription_repository)

    # Suppliers

    def memory_tenant_supplier(self) -> MemoryTenantSupplier:
        return MemoryTenantSupplier()

    def memory_migration_supplier(self) -> MemoryMigrationSupplier:
        return MemoryMigrationSupplier()
