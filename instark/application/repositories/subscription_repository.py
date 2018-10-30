from ..models import Subscription
from .repository import Repository
from .memory_repository import MemoryRepository


class SubscriptionRepository(Repository[Subscription]):
    """Device Channel Repository"""


class MemorySubscriptionRepository(
        MemoryRepository[Subscription], SubscriptionRepository):
    """Memory Subscription Repository"""
