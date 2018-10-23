from abc import ABC, abstractmethod
from ..repositories import DeviceRepository
from .types import DeviceDictList, ChannelDictList, SearchDomain


class InstarkReporter(ABC):

    @abstractmethod
    def search_devices(self, domain: SearchDomain) -> DeviceDictList:
        """Search Instark's devices"""


class MemoryInstarkReporter(InstarkReporter):

    def __init__(self, device_repository: DeviceRepository,
                 channel_repository) -> None:
        self.device_repository = device_repository
        self.channel_repository = channel_repository

    def search_devices(self, domain: SearchDomain) -> DeviceDictList:
        return [vars(device) for device in
                self.device_repository.search(domain)]

    def search_channels(self, domain: SearchDomain) -> ChannelDictList:
        return [vars(channel) for channel in
                self.channel_repository.search(domain)]
