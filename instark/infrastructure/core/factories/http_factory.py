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
from ...web.middleware import Authenticate
from ...core.crypto import JwtSupplier
from ...delivery import FirebaseDeliveryService
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
    
    def jwt_supplier(self) -> JwtSupplier:
        secret = 'secret'
        secret_file = self.config.get('secrets', {}).get('jwt')
        # if secret_file:
        #     secret = Path(secret_file).read_text().strip()
        return JwtSupplier(secret)

    def firebase_delivery_service(self) -> FirebaseDeliveryService:
       
       
        default_firebase_credentials_path = str(Path.home().joinpath(
            'firebase_credentials.json'))
        firebase_credentials_path = self.config.get(
            'firebase_credentials_path', default_firebase_credentials_path)


        return FirebaseDeliveryService(firebase_credentials_path)
