from filtrark.sql_parser import SqlParser
from ....application.utilities import TenantProvider
from ....application.services import AuthService
from ....application.models import (
    channel, device, message, subscription)
from ....application.repositories import (
    ChannelRepository, DeviceRepository, MessageRepository,
    SubscriptionRepository)
from .connection import ConnectionManager
from .sql_repository import SqlRepository


class SqlChannelRepository(SqlRepository, ChannelRepository):
    """Sql Channel Repository"""

    def __init__(self, tenant_provider: TenantProvider,
                 auth_service: AuthService,
                 connection_manager: ConnectionManager,
                 parser: SqlParser) -> None:
        super().__init__('channels', channel, tenant_provider,
                         auth_service, connection_manager, parser)


class SqlDeviceRepository(SqlRepository, DeviceRepository):
    """Sql Device Repository"""

    def __init__(self, tenant_provider: TenantProvider,
                 auth_service: AuthService,
                 connection_manager: ConnectionManager,
                 parser: SqlParser) -> None:
        super().__init__('devices', device, tenant_provider,
                         auth_service, connection_manager, parser)


class SqlMessageRepository(SqlRepository, MessageRepository):
    """Sql Message Repository"""

    def __init__(self, tenant_provider: TenantProvider,
                 auth_service: AuthService,
                 connection_manager: ConnectionManager,
                 parser: SqlParser) -> None:
        super().__init__('messages', message, tenant_provider,
                         auth_service, connection_manager, parser)


class SqlSubscriptionRepository(SqlRepository, SubscriptionRepository):
    """Sql Subscription Repository"""

    def __init__(self, tenant_provider: TenantProvider,
                 auth_service: AuthService,
                 connection_manager: ConnectionManager,
                 parser: SqlParser) -> None:
        super().__init__('subscriptions', subscription, tenant_provider,
                         auth_service, connection_manager, parser)


