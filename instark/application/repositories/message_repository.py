from ..models import Message
from .repository.repository import Repository
from .repository.memory_repository import MemoryRepository


class MessageRepository(Repository[Message]):
    """Message Repository"""


class MemoryMessageRepository(MemoryRepository[Message], MessageRepository):
    """Memory Message Repository"""
