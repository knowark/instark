from ..config import Config
from .factory import Factory
from ...application.utilities import (Tenant,
    QueryParser, TenantProvider, StandardTenantProvider,
    AuthProvider, StandardAuthProvider, 
    TransactionManager, MemoryTransactionManager)
from ...application.repositories import (
    DeviceRepository, MemoryDeviceRepository,
    ChannelRepository, MemoryChannelRepository,
    SubscriptionRepository, MemorySubscriptionRepository,
    MessageRepository, MemoryMessageRepository)
from ...application.services import (MemoryDeliveryService,
    DeliveryService)
from ...application.coordinators import (
    RegistrationCoordinator, SubscriptionCoordinator, NotificationCoordinator,
    SessionCoordinator)
from ...application.informers import StandardInstarkInformer
from ...infrastructure.core import (
    TenantSupplier, MemoryTenantSupplier,
    SetupSupplier, MemorySetupSupplier)

class MemoryFactory(Factory):
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
            query_parser, tenant_provider, auth_provider )

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

    # Coordinators

    def registration_coordinator(
        self, device_repository: DeviceRepository,
        transaction_manager: TransactionManager
    ) -> RegistrationCoordinator:
        return transaction_manager(RegistrationCoordinator)(
            device_repository)

    def subscription_coordinator(
        self, channel_repository: ChannelRepository,
        device_repository: DeviceRepository,
        subscription_repository: SubscriptionRepository,
        delivery_service: DeliveryService,
        transaction_manager: TransactionManager
    ) -> SubscriptionCoordinator:
        return transaction_manager(SubscriptionCoordinator)(
            channel_repository,
            device_repository, subscription_repository,
            delivery_service)

    def notification_coordinator(
        self, channel_repository: ChannelRepository,
        device_repository: DeviceRepository,
        message_repository: MessageRepository,
        delivery_service: DeliveryService,
        transaction_manager: TransactionManager
    ) -> NotificationCoordinator:
        return transaction_manager(NotificationCoordinator)(
            channel_repository,
            device_repository, message_repository, delivery_service)

    def session_coordinator(
        self, tenant_provider: TenantProvider, 
        auth_provider: AuthProvider
    ) -> SessionCoordinator:
        return SessionCoordinator(tenant_provider, auth_provider)

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


    #Suppliers

    def memory_tenant_supplier(self) -> MemoryTenantSupplier:
        return MemoryTenantSupplier()

    def memory_setup_supplier(self) -> MemorySetupSupplier:
        return MemorySetupSupplier()

     