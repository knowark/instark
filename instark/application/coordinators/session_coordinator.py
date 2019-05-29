from typing import Dict, Any
from ..utilities import TenantProvider, Tenant


class SessionCoordinator:
    def __init__(self, tenant_provider: TenantProvider) -> None:
        self.tenant_provider = tenant_provider

    def set_tenant(self, tenant_dict: Dict[str, Any]) -> None:
        tenant = Tenant(**tenant_dict)
        self.tenant_provider.setup(tenant)

    def get_tenant(self) -> Dict[str, Any]:
        tenant = self.tenant_provider.tenant
        return vars(tenant)