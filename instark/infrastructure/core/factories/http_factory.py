from pathlib import Path
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
from ...delivery import FirebaseDeliveryService
from ..configuration import Config
from ..tenancy import TenantSupplier, JsonTenantSupplier, MemoryTenantSupplier
from .memory_factory import MemoryFactory


class HttpFactory(MemoryFactory):
    def __init__(self, config: Config) -> None:
        super().__init__(config)

    def json_tenant_supplier(self) -> TenantSupplier:
        catalog_path = self.config['tenancy']['json']
        # directory_data = self.config['data']['json']['default']
        directory_data = ''
        return JsonTenantSupplier(catalog_path, directory_data)

    def firebase_delivery_service(self) -> FirebaseDeliveryService:

        default_firebase_credentials_path = str(Path.home().joinpath(
            'firebase_credentials.json'))
        firebase_credentials_path = self.config.get(
            'firebase_credentials_path', default_firebase_credentials_path)

        return FirebaseDeliveryService(firebase_credentials_path)
