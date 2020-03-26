#from abc import ABC, abstractmethod
import time
from uuid import uuid4
from collections import defaultdict
from typing import List, Dict, TypeVar, Optional, Generic, Union, Any
from ..models import T
from ..utilities.tenancy import TenantProvider, StandardTenantProvider
from ..services.auth import AuthService, StandardAuthService
from ..utilities.query_parser import QueryParser
from ..utilities.types import T, QueryDomain
from ..utilities.exceptions import EntityNotFoundError
from .repository import Repository


class MemoryRepository(Repository, Generic[T]):
    def __init__(self,  parser: QueryParser,
                 tenant_provider: TenantProvider,
                 auth_service: AuthService) -> None:
        self.data: Dict[str, Dict[str, T]] = defaultdict(dict)
        self.parser = parser
        self.tenant_provider: TenantProvider = tenant_provider
        self.auth_service: AuthService = auth_service
        self.max_items = 10_000

    async def get(self, id: str) -> T:
        item = self.data[self._location].get(id)
        if not item:
            raise EntityNotFoundError(
                f"The entity with id {id} was not found.")
        return item

    async def add(self, item: T) -> T:
        setattr(item, 'id', getattr(item, 'id') or str(uuid4()))
        self.data[self._location][getattr(item, 'id')] = item
        return item

    async def search(self, domain: QueryDomain, limit=0, offset=0) -> List[T]:
        items = []
        limit = int(limit) if limit > 0 else 100
        offset = int(offset) if offset > 0 else 0
        filter_function = self.parser.parse(domain)
        for item in list(self.data[self._location].values()):
            if filter_function(item):
                items.append(item)

        items = items[:limit]
        items = items[offset:]

        return items

    async def remove(self, item: T) -> bool:
        id = getattr(item, 'id')
        if id not in self.data[self._location]:
            return False
        del self.data[self._location][id]
        return True

    def load(self, data: Dict[str, Dict[str, T]]) -> None:
        self.data = data

    @property
    def _location(self) -> str:
        return self.tenant_provider.tenant.location
