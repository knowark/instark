from ..models import Subscription
from .repository.repository import Repository
from .repository.memory_repository import MemoryRepository


class SubscriptionRepository(Repository[Subscription]):
    """Device Channel Repository"""


class MemorySubscriptionRepository(
        MemoryRepository[Subscription], SubscriptionRepository):
    """Memory Subscription Repository"""
