from ..models import DeviceChannel
from .repository import Repository
from .memory_repository import MemoryRepository


class DeviceChannelRepository(Repository[DeviceChannel]):
    """Device Channel Repository"""


class MemoryDeviceChannelRepository(
        MemoryRepository[DeviceChannel], DeviceChannelRepository):
    """Memory Device Channel Repository"""
