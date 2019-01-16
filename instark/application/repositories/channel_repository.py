from ..models import Channel
from .repository.repository import Repository
from .repository.memory_repository import MemoryRepository


class ChannelRepository(Repository[Channel]):
    """Channel Repository"""


class MemoryChannelRepository(MemoryRepository[Channel], ChannelRepository):
    """Memory Channel Repository"""
