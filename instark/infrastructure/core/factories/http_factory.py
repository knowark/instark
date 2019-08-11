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
from ..tenancy import TenantSupplier, JsonTenantSupplier, MemoryTenantSupplier
from .memory_factory import MemoryFactory


class HttpFactory(MemoryFactory):
    def __init__(self, config: Config) -> None:
        super().__init__(config)
        # self.config = config

    def middleware_authenticate(
            self, jwt_supplier: JwtSupplier,
            tenant_supplier: TenantSupplier,
            session_coordinator: SessionCoordinator) -> Authenticate:
        return Authenticate(
            jwt_supplier, tenant_supplier, session_coordinator)
    
    def json_tenant_supplier(self) -> TenantSupplier:
        # catalog_path = self.config['tenancy']['json']
        catalog_path = '/opt/instark/tenants.json'
        # directory_data = self.config['data']['json']['default']
        directory_data = ''
        return JsonTenantSupplier(catalog_path, directory_data)

    def jwt_supplier(self) -> JwtSupplier:
        secret = 'secret'
        secret_file = self.config.get('secrets', {}).get('jwt')
        if secret_file:
            secret = Path(secret_file).read_text().strip()
        return JwtSupplier(secret)

    def firebase_delivery_service(self) -> FirebaseDeliveryService:
       
       
        default_firebase_credentials_path = str(Path.home().joinpath(
            'firebase_credentials.json'))
        firebase_credentials_path = self.config.get(
            'firebase_credentials_path', default_firebase_credentials_path)


        return FirebaseDeliveryService(firebase_credentials_path)
