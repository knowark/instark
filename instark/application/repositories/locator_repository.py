from ..models import Locator
from .repository.repository import Repository
from .repository.memory_repository import MemoryRepository


class LocatorRepository(Repository[Locator]):
    """Locator Repository"""


class MemoryLocatorRepository(
        MemoryRepository[Locator], LocatorRepository):
    """Memory Locator Repository"""
