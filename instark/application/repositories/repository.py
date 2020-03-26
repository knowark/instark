from abc import ABC, abstractmethod
from typing import List, TypeVar, Optional, Generic, Dict
from ..utilities.types import T, QueryDomain


class Repository(ABC, Generic[T]):

    """@abstractmethod
    async def get(self, id: str) -> T:
        "Get method to be implemented."""

    @abstractmethod
    async def add(self, item: T) -> T:
        "Add method to be implemented."

    @abstractmethod
    async def search(self, domain: QueryDomain,
               limit: int = 0, offset: int = 0) -> List[T]:
        "Search items matching a query domain"

    @abstractmethod
    async def remove(self, user: T) -> bool:
        "Remove method to be implemented."

