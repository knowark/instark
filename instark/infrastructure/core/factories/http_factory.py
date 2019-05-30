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
from ..configuration import Config
from ..tenancy import TenantSupplier, MemoryTenantSupplier
from .memory_factory import MemoryFactory


class HttpFactory(MemoryFactory):
    def __init__(self, config: Config) -> None:
        self.config = config

    def middleware_authenticate(
            self, jwt_supplier: JwtSupplier,
            tenant_supplier: TenantSupplier,
            session_coordinator: SessionCoordinator) -> Authenticate:
        return Authenticate(
            jwt_supplier, tenant_supplier, session_coordinator)

    def jwt_supplier(self) -> JwtSupplier:
        secret = self.access_config['secret']
        return JwtSupplier(secret)
