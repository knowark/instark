from modelark import Repository, MemoryRepository


class ChannelRepository(Repository):
    """Channel Repository"""


class MemoryChannelRepository(
        MemoryRepository, ChannelRepository):
    """Memory Channel Repository"""


class DeviceRepository(Repository):
    """Device Repository"""


class MemoryDeviceRepository(
        MemoryRepository, DeviceRepository):
    """Memory Device Repository"""


class MessageRepository(Repository):
    """Message Repository"""


class MemoryMessageRepository(
        MemoryRepository, MessageRepository):
    """Message Option Repository"""


class SubscriptionRepository(Repository):
    """Subscription Repository"""


class MemorySubscriptionRepository(
        MemoryRepository, SubscriptionRepository):
    """Memory Subscription Repository"""
