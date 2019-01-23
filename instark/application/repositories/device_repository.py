from ..models import Device
from .repository.repository import Repository
from .repository.memory_repository import MemoryRepository


class DeviceRepository(Repository[Device]):
    """Device Repository"""


class MemoryDeviceRepository(MemoryRepository[Device], DeviceRepository):
    """Memory Device Repository"""
