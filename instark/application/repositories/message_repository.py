from ..models import Message
from .repository import Repository
from .memory_repository import MemoryRepository


class MessageRepository(Repository[Message]):
    """Message Repository"""


class MemoryMessageRepository(MemoryRepository[Message], MessageRepository):
    """Memory Message Repository"""
