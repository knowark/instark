from abc import ABC, abstractmethod
from ..repositories import DeviceRepository
from .types import DeviceDictList, SearchDomain


class InstarkReporter(ABC):

    @abstractmethod
    def search_devices(self, domain: SearchDomain) -> DeviceDictList:
        """Search Instark's devices"""


class MemoryInstarkReporter(InstarkReporter):

    def __init__(self, device_repository: DeviceRepository) -> None:
        self.device_repository = device_repository

    def search_devices(self, domain: SearchDomain) -> DeviceDictList:
        return [vars(device) for device in
                self.device_repository.search(domain)]
