from abc import ABC, abstractmethod
from typing import List, TypeVar, Optional, Generic, Dict
from ...utilities.types import T, QueryDomain


class Repository(ABC, Generic[T]):

    @abstractmethod
    def get(self, id: str) -> T:
        "Get method to be implemented."

    @abstractmethod
    def add(self, item: T) -> T:
        "Add method to be implemented."

    @abstractmethod
    def search(self, domain: QueryDomain,
               limit: int = 0, offset: int = 0) -> List[T]:
        "Search items matching a query domain"

    @abstractmethod
    def remove(self, user: T) -> bool:
        "Remove method to be implemented."

    @abstractmethod
    def load(self, items: Dict[str, T]) -> None:
        "load method to be implemented."