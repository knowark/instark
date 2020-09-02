from pytest import fixture
from instark.application.domain.common import (
    QueryParser, TenantProvider, StandardTenantProvider)


@fixture
def tenant_provider() -> TenantProvider:
    return StandardTenantProvider()
