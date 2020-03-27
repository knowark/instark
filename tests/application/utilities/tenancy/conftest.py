from pytest import fixture
from instark.application.utilities import (
    QueryParser, TenantProvider, StandardTenantProvider)


@fixture
def tenant_provider() -> TenantProvider:
    return StandardTenantProvider()
