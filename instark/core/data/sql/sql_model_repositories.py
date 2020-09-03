from filtrark.sql_parser import SqlParser
from modelark import SqlRepository
from ....application.domain.common import (
    TenantProvider, AuthProvider)
from ....application.domain.models import (
    Channel, Device, Message, Subscription)
from ....application.domain.repositories import (
    ChannelRepository, DeviceRepository, MessageRepository,
    SubscriptionRepository)
from .connection import ConnectionManager


class SqlChannelRepository(SqlRepository, ChannelRepository):
    """Sql Channel Repository"""

    def __init__(self, tenant_provider: TenantProvider,
                 auth_provider: AuthProvider,
                 connection_manager: ConnectionManager,
                 parser: SqlParser) -> None:
        super().__init__('channels', Channel, tenant_provider,
                         auth_provider, connection_manager, parser)

    def _order_by(self) -> str:
        return "ORDER BY data->>'name' ASC NULLS LAST"


class SqlDeviceRepository(SqlRepository, DeviceRepository):
    """Sql Device Repository"""

    def __init__(self, tenant_provider: TenantProvider,
                 auth_provider: AuthProvider,
                 connection_manager: ConnectionManager,
                 parser: SqlParser) -> None:
        super().__init__('devices', Device, tenant_provider,
                         auth_provider, connection_manager, parser)

    def _order_by(self) -> str:
        return "ORDER BY data->>'name' ASC NULLS LAST"


class SqlMessageRepository(SqlRepository, MessageRepository):
    """Sql Message Repository"""

    def __init__(self, tenant_provider: TenantProvider,
                 auth_provider: AuthProvider,
                 connection_manager: ConnectionManager,
                 parser: SqlParser) -> None:
        super().__init__('messages', Message, tenant_provider,
                         auth_provider, connection_manager, parser)


class SqlSubscriptionRepository(SqlRepository, SubscriptionRepository):
    """Sql Subscription Repository"""

    def __init__(self, tenant_provider: TenantProvider,
                 auth_provider: AuthProvider,
                 connection_manager: ConnectionManager,
                 parser: SqlParser) -> None:
        super().__init__('subscriptions', Subscription, tenant_provider,
                         auth_provider, connection_manager, parser)
