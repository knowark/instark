from abc import ABC, abstractmethod
from typing import List, TypeVar, Optional, Generic
from .types import T


class Repository(ABC, Generic[T]):

    @abstractmethod
    def get(self, id: str) -> Optional[T]:
        "Get method to be implemented."

    @abstractmethod
    def add(self, item: T) -> bool:
        "Add method to be implemented."

    @abstractmethod
    def search(self) -> List[T]:
        "Search users matching a query domain"

    @abstractmethod
    def remove(self, user: T) -> bool:
        "Remove method to be implemented."
