import os
from pathlib import Path
from filtrark import SqlParser, SafeEval
from ...application.utilities import QueryParser, TenantProvider, AuthProvider
from ..data import (
    ConnectionManager, DefaultConnectionManager, SqlTransactionManager,
    SqlQuestionnaireRepository, SqlQuestionRepository, SqlOptionRepository,
    SqlAssessmentRepository, SqlAnswerRepository, SqlSelectionRepository)
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
            options = {'name': zone, 'dsn': config['dsn']}
            settings.append(options)

        return DefaultConnectionManager(settings)

    def sql_transaction_manager(
        self, connection_manager: ConnectionManager,
        tenant_provider: TenantProvider
    ) -> SqlTransactionManager:
        return SqlTransactionManager(connection_manager, tenant_provider)

    def sql_questionnaire_repository(
            self, tenant_provider: TenantProvider,
            auth_provider: AuthProvider,
            connection_manager: ConnectionManager,
            sql_parser: SqlParser) -> SqlQuestionnaireRepository:
        return SqlQuestionnaireRepository(
            tenant_provider, auth_provider, connection_manager, sql_parser)

    def sql_question_repository(
            self, tenant_provider: TenantProvider,
            auth_provider: AuthProvider,
            connection_manager: ConnectionManager,
            sql_parser: SqlParser) -> SqlQuestionRepository:

        return SqlQuestionRepository(
            tenant_provider, auth_provider, connection_manager, sql_parser)

    def sql_option_repository(
            self, tenant_provider: TenantProvider,
            auth_provider: AuthProvider,
            connection_manager: ConnectionManager,
            sql_parser: SqlParser) -> SqlOptionRepository:

        return SqlOptionRepository(
            tenant_provider, auth_provider, connection_manager, sql_parser)

    def sql_assessment_repository(
            self, tenant_provider: TenantProvider,
            auth_provider: AuthProvider,
            connection_manager: ConnectionManager,
            sql_parser: SqlParser) -> SqlAssessmentRepository:

        return SqlAssessmentRepository(
            tenant_provider, auth_provider, connection_manager, sql_parser)

    def sql_answer_repository(
            self, tenant_provider: TenantProvider,
            auth_provider: AuthProvider,
            connection_manager: ConnectionManager,
            sql_parser: SqlParser) -> SqlAnswerRepository:

        return SqlAnswerRepository(
            tenant_provider, auth_provider, connection_manager, sql_parser)

    def sql_selection_repository(
            self, tenant_provider: TenantProvider,
            auth_provider: AuthProvider,
            connection_manager: ConnectionManager,
            sql_parser: SqlParser) -> SqlSelectionRepository:

        return SqlSelectionRepository(
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
