from .trial_factory import TrialFactory
from ..configuration import Config
from ..tenancy import MemoryTenantSupplier
from ....application.utilities import Tenant


class MemoryFactory(TrialFactory):
    def __init__(self, config: Config) -> None:
        self.config = config

    def trial_memory_tenant_supplier(self) -> MemoryTenantSupplier:
        memory_tenant_supplier = MemoryTenantSupplier()
        memory_tenant_supplier.arranger.cataloguer.catalog = {
            "1": Tenant(id="1", name="default", location="default")
        }
        return memory_tenant_supplier
