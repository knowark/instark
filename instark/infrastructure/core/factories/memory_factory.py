from pathlib import Path
from .factory import Factory
from ..configuration import Config
from ..tenancy import TenantSupplier, MemoryTenantSupplier
from ....application.utilities import (
    QueryParser, TenantProvider, StandardTenantProvider)
from ....application.repositories import (
    DeviceRepository, MemoryDeviceRepository,
    ChannelRepository, MemoryChannelRepository,
    SubscriptionRepository, MemorySubscriptionRepository,
    MessageRepository, MemoryMessageRepository)
from ....application.services import (
    AuthService, StandardAuthService, StandardIdService, MemoryDeliveryService,
    DeliveryService, IdService)
from ....application.coordinators import (
    RegistrationCoordinator, SubscriptionCoordinator, NotificationCoordinator,
    SessionCoordinator)
from ....application.informers import StandardInstarkInformer
from ...web.middleware import Authenticate
from ...core.crypto import JwtSupplier


class MemoryFactory(Factory):
    def __init__(self, config: Config) -> None:
        self.config = config

    # Security

    def middleware_authenticate(
            self, jwt_supplier: JwtSupplier,
            tenant_supplier: TenantSupplier,
            session_coordinator: SessionCoordinator) -> Authenticate:
        return Authenticate(
            jwt_supplier, tenant_supplier, session_coordinator)

    def jwt_supplier(self) -> JwtSupplier:
        secret = 'secret'
        secret_file = self.config.get('secrets', {}).get('jwt')
        if secret_file:
            secret = Path(secret_file).read_text().strip()
        return JwtSupplier(secret)

    # Repositories

    def query_parser(self) -> QueryParser:
        return QueryParser()

    def memory_device_repository(
        self, query_parser: QueryParser,
        tenant_provider: TenantProvider
    ) -> MemoryDeviceRepository:
        return MemoryDeviceRepository(query_parser, tenant_provider)

    def memory_channel_repository(
        self, query_parser: QueryParser,
        tenant_provider: TenantProvider
    ) -> MemoryChannelRepository:
        return MemoryChannelRepository(query_parser, tenant_provider)

    def memory_subscription_repository(
        self, query_parser: QueryParser,
        tenant_provider: TenantProvider
    ) -> MemorySubscriptionRepository:
        return MemorySubscriptionRepository(query_parser, tenant_provider)

    def memory_message_repository(
        self, query_parser: QueryParser,
        tenant_provider: TenantProvider
    ) -> MemoryMessageRepository:
        return MemoryMessageRepository(query_parser, tenant_provider)

    # Tenancy

    def memory_tenant_supplier(self) -> MemoryTenantSupplier:
        return MemoryTenantSupplier()

    def standard_tenant_provider(self) -> StandardTenantProvider:
        return StandardTenantProvider()

    # Services

    def memory_delivery_service(self) -> MemoryDeliveryService:
        return MemoryDeliveryService('Fake Response')

    def standart_id_service(self) -> StandardIdService:
        return StandardIdService()

    def memory_auth_service(self) -> StandardAuthService:
        dominion = self.config['authorization']['dominion']
        return StandardAuthService(dominion)

    # Coordinators

    def registration_coordinator(
        self, id_service: IdService,
        device_repository: DeviceRepository
    ) -> RegistrationCoordinator:
        return RegistrationCoordinator(id_service, device_repository)

    def subscription_coordinator(
        self, id_service: IdService,
        channel_repository: ChannelRepository,
        device_repository: DeviceRepository,
        device_channel_repository: SubscriptionRepository,
        delivery_service: DeliveryService
    ) -> SubscriptionCoordinator:
        return SubscriptionCoordinator(id_service, channel_repository,
                                       device_repository,
                                       device_channel_repository,
                                       delivery_service)

    def notification_coordinator(
        self, id_service: IdService,
        channel_repository: ChannelRepository,
        device_repository: DeviceRepository,
        message_repository: MessageRepository,
        delivery_service: DeliveryService
    ) -> NotificationCoordinator:
        return NotificationCoordinator(id_service, channel_repository,
                                       device_repository, message_repository,
                                       delivery_service)

    def session_coordinator(
        self, tenant_provider: TenantProvider, auth_service: AuthService
    ) -> SessionCoordinator:
        return SessionCoordinator(tenant_provider, auth_service)

    # Reporters

    def memory_instark_informer(
        self, device_repository: DeviceRepository,
        channel_repository: ChannelRepository,
        message_repository: MessageRepository,
        device_channel_repository: SubscriptionRepository
    ) -> StandardInstarkInformer:
        return StandardInstarkInformer(device_repository, channel_repository,
                                       message_repository,
                                       device_channel_repository)
