from .trial_factory import TrialFactory
from ..configuration import Config
from ..core.tenancy import MemoryTenantSupplier
from ...application.utilities import Tenant


class MemoryFactory(TrialFactory):
    def __init__(self, config: Config) -> None:
        super().__init__(config)

    def trial_memory_tenant_supplier(self) -> MemoryTenantSupplier:
        memory_tenant_supplier = MemoryTenantSupplier()
        memory_tenant_supplier.arranger.cataloguer.catalog = {
            "1": Tenant(id="1", name="origin", location="origin")
        }
        return memory_tenant_supplier
