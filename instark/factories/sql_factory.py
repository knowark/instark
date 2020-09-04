import os
from pathlib import Path
from filtrark import SqlParser, SafeEval
from ..application.domain.common import (QueryParser, TenantProvider,
                                         AuthProvider)
from ..core.data import (
    ConnectionManager, DefaultConnectionManager, SqlTransactionManager,
    SqlChannelRepository, SqlDeviceRepository, SqlMessageRepository,
    SqlSubscriptionRepository)
from ..core import Config
from ..core import (TenantSupplier, SchemaTenantSupplier,
                    SchemaMigrationSupplier, SchemaConnection)
from .base_factory import BaseFactory

from ..presenters.delivery import FirebaseDeliveryService


class SqlFactory(BaseFactory):
    def __init__(self, config: Config) -> None:
        super().__init__(config)

    def sql_query_parser(self) -> SqlParser:
        return SqlParser(SafeEval(), jsonb_collection='data')

    def sql_connection_manager(self) -> DefaultConnectionManager:
        settings = []
        for zone, config in self.config['zones'].items():
            options = {'name': zone, 'dsn': config['dsn']}
            settings.append(options)

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
        zones = {key: value['dsn'] for key, value in
                 self.config['zones'].items()}
        connection = SchemaConnection(self.config['tenancy']['dsn'])
        return SchemaTenantSupplier(connection, zones)

    def schema_migration_supplier(
            self, tenant_supplier: TenantSupplier) -> SchemaMigrationSupplier:
        zones = {key: value['dsn'] for key, value in
                 self.config['zones'].items()}
        return SchemaMigrationSupplier(zones, tenant_supplier)

    # services

    def firebase_delivery_service(self) -> FirebaseDeliveryService:

        # default_firebase_credentials_path = str(Path.home().joinpath(
        #     'firebase_credentials.json'))

        default_firebase_credentials_path = str(Path.home().joinpath(
            'proser-2020-firebase-adminsdk-554ie-41811eb8ea.json'))

        firebase_credentials_path = self.config.get(
            'firebase_credentials_path', default_firebase_credentials_path)

        return FirebaseDeliveryService(firebase_credentials_path)
