from filtrark.sql_parser import SqlParser
from ....application.utilities import (
    TenantProvider, AuthProvider)
from ....application.models import (
    Questionnaire, Question, Option, Assessment, Answer, Selection)
from ....application.repositories import (
    QuestionnaireRepository, QuestionRepository, OptionRepository,
    AssessmentRepository, AnswerRepository, SelectionRepository)
from .connection import ConnectionManager
from .sql_repository import SqlRepository


class SqlQuestionnaireRepository(SqlRepository, QuestionnaireRepository):
    """Sql Questionnaire Repository"""

    def __init__(self, tenant_provider: TenantProvider,
                 auth_provider: AuthProvider,
                 connection_manager: ConnectionManager,
                 parser: SqlParser) -> None:
        super().__init__('questionnaires', Questionnaire, tenant_provider,
                         auth_provider, connection_manager, parser)


class SqlQuestionRepository(SqlRepository, QuestionRepository):
    """Sql Question Repository"""

    def __init__(self, tenant_provider: TenantProvider,
                 auth_provider: AuthProvider,
                 connection_manager: ConnectionManager,
                 parser: SqlParser) -> None:
        super().__init__('questions', Question, tenant_provider,
                         auth_provider, connection_manager, parser)


class SqlOptionRepository(SqlRepository, OptionRepository):
    """Sql Option Repository"""

    def __init__(self, tenant_provider: TenantProvider,
                 auth_provider: AuthProvider,
                 connection_manager: ConnectionManager,
                 parser: SqlParser) -> None:
        super().__init__('options', Option, tenant_provider,
                         auth_provider, connection_manager, parser)


class SqlAssessmentRepository(SqlRepository, AssessmentRepository):
    """Sql Assessment Repository"""

    def __init__(self, tenant_provider: TenantProvider,
                 auth_provider: AuthProvider,
                 connection_manager: ConnectionManager,
                 parser: SqlParser) -> None:
        super().__init__('assessments', Assessment, tenant_provider,
                         auth_provider, connection_manager, parser)


class SqlAnswerRepository(SqlRepository, AnswerRepository):
    """Sql Answer Repository"""

    def __init__(self, tenant_provider: TenantProvider,
                 auth_provider: AuthProvider,
                 connection_manager: ConnectionManager,
                 parser: SqlParser) -> None:
        super().__init__('answers', Answer, tenant_provider,
                         auth_provider, connection_manager, parser)


class SqlSelectionRepository(SqlRepository, SelectionRepository):
    """Sql Selection Repository"""

    def __init__(self, tenant_provider: TenantProvider,
                 auth_provider: AuthProvider,
                 connection_manager: ConnectionManager,
                 parser: SqlParser) -> None:
        super().__init__('selections', Selection, tenant_provider,
                         auth_provider, connection_manager, parser)
