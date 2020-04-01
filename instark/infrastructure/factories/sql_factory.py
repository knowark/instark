import os
from pathlib import Path
from filtrark import SqlParser, SafeEval
from ...application.utilities import (QueryParser, TenantProvider,
                                      AuthProvider)
from ..data import (
    ConnectionManager, DefaultConnectionManager, SqlTransactionManager,
    SqlChannelRepository, SqlDeviceRepository, SqlMessageRepository,
    SqlSubscriptionRepository)
from ..config import Config
from ..core import SchemaTenantSupplier, SchemaSetupSupplier
from .memory_factory import MemoryFactory


class SqlFactory(MemoryFactory):
    def __init__(self, config: Config) -> None:
        super().__init__(config)

    def sql_query_parser(self) -> SqlParser:
        return SqlParser(SafeEval())

    def sql_connection_manager(self) -> DefaultConnectionManager:
        settings = []
        for zone, config in self.config['zones'].items():
            Messages = {'name': zone, 'dsn': config['dsn']}
            settings.append(Messages)

        return DefaultConnectionManager(settings)

    def sql_transaction_manager(
        self, connection_manager: ConnectionManager,
        tenant_provider: TenantProvider
    ) -> SqlTransactionManager:
        return SqlTransactionManager(connection_manager, tenant_provider)

    def sql_channel_repository(
            self, tenant_provider: TenantProvider,
            auth_provider: AuthProvider,
            connection_manager: ConnectionManager,
            sql_parser: SqlParser) -> SqlChannelRepository:
        return SqlChannelRepository(
            tenant_provider, auth_provider, connection_manager, sql_parser)

    def sql_device_repository(
            self, tenant_provider: TenantProvider,
            auth_provider: AuthProvider,
            connection_manager: ConnectionManager,
            sql_parser: SqlParser) -> SqlDeviceRepository:
        return SqlDeviceRepository(
            tenant_provider, auth_provider, connection_manager, sql_parser)

    def sql_message_repository(
            self, tenant_provider: TenantProvider,
            auth_provider: AuthProvider,
            connection_manager: ConnectionManager,
            sql_parser: SqlParser) -> SqlMessageRepository:
        return SqlMessageRepository(
            tenant_provider, auth_provider, connection_manager, sql_parser)

    def sql_subscription_repository(
            self, tenant_provider: TenantProvider,
            auth_provider: AuthProvider,
            connection_manager: ConnectionManager,
            sql_parser: SqlParser) -> SqlSubscriptionRepository:
        return SqlSubscriptionRepository(
            tenant_provider, auth_provider, connection_manager, sql_parser)

    def schema_tenant_supplier(self) -> SchemaTenantSupplier:
        catalog = self.config['tenancy']['dsn']
        zones = {key: value['dsn'] for key, value in
                 self.config['zones'].items()}
        return SchemaTenantSupplier(catalog, zones)

    def schema_setup_supplier(self) -> SchemaSetupSupplier:
        zones = {key: value['dsn'] for key, value in
                 self.config['zones'].items()}
        return SchemaSetupSupplier(zones)
