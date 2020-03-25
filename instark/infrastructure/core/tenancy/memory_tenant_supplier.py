from typing import Dict, Any
from tenark.models import Tenant
from tenark.resolver import resolve_managers
from .tenant_supplier import TenantSupplier

class MemoryTenantSupplier(TenantSupplier):

    def __init__(self) -> None:
        #cataloguer = resolve_cataloguer({})
        #self.provider = resolve_provider({
        #    'cataloguer': cataloguer
        #})
        #self.arranger = resolve_arranger({
        #    'cataloguer': cataloguer
        #})
        self.arranger, self.provider = resolve_managers({})

    def get_tenant(self, tenant_id: str) -> Dict[str, Any]:
        return self.provider.get_tenant(tenant_id)

    def create_tenant(self, tenant_dict: Dict[str, Any]) -> None:
        self.arranger.create_tenant(tenant_dict)

    def search_tenants(self, domain):
        return self.provider.search_tenants(domain)