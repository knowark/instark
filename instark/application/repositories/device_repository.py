from ..models import Device
from .repository import Repository
from .memory_repository import MemoryRepository


class DeviceRepository(Repository[Device]):
    """Device Repository"""


class MemoryDeviceRepository(MemoryRepository[Device], DeviceRepository):
    """Memory Device Repository"""
